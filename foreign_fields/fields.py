from django.forms.fields import CharField
from django.forms.widgets import Textarea
from django.core.exceptions import ValidationError
from django.apps import apps
from django.db.models import utils
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from itertools import chain

RECURSIVE_RELATIONSHIP_CONSTANT = 'self'

class ForeignField(CharField):
    def __init__(self, to, max_length=None, min_length=None, strip=True, empty_value='', selector='', **kwargs):
        super().__init__(**kwargs)
        self.selector = selector
        self.to = ''

        try:
            self.to = apps.get_model(*utils.make_model_tuple(to))
        except AttributeError:
            assert isinstance(to, str), (
                "%s(%r) is invalid. First parameter to ForeignField must be "
                "either a model, a model name, or the string %r" % (
                    self.__class__.__name__, to,
                    RECURSIVE_RELATIONSHIP_CONSTANT,
                )
            )

        self.error_messages['target_exists'] = _('The %s must exist.' % self.to.__name__) 
        self.error_messages['unique_target'] = _('The %s must be unique.' % self.to.__name__) 
        
    def to_python(self, value):
        """Returns an object."""
        if value in self.empty_values:
            return self.empty_value

        objects = self.to.objects.filter(**{self.selector: value})

        self.check_queryset_count(objects)

        return objects.first()

    def check_queryset_count(self, queryset):
        count = queryset.count()

        if count < 1:
            raise ValidationError(self.error_messages['target_exists'], code='target_exists')
        if count > 1:
            raise ValidationError(self.error_messages['unique_target'], code='unique_target')

class TextAreaToManyField(ForeignField):
    widget = Textarea

    def to_python(self, values):
        """Returns a queryset."""
        if values in self.empty_values:
            return []

        identifier_list = []

        for value in values.splitlines():
            objects = self.to.objects.filter(**{self.selector: value})

            self.check_queryset_count(objects)

            identifier_list.append(objects.first().id)

        return identifier_list
