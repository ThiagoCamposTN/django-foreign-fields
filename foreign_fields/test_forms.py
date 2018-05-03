from django.forms import (CheckboxSelectMultiple, ModelForm, NumberInput,
                          SelectDateWidget, Textarea)

from .fields import TextAreaToManyField, ForeignField
from .test_models import Referrer, Target


class ForeignFormTestDateTime(ModelForm):
    foreign = ForeignField(to='foreign_fields.Target', selector="datetimenew")

    class Meta:
        model = Referrer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ForeignFormTestDateTime, self).__init__(*args, **kwargs)
        self.fields['foreign'].widget = SelectDateWidget()

class ForeignFormTestInteger(ModelForm):
    foreign = ForeignField(to='foreign_fields.Target', selector="integer")

    class Meta:
        model = Referrer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ForeignFormTestInteger, self).__init__(*args, **kwargs)
        self.fields['foreign'].widget = NumberInput()

class ForeignFormTestDefaultWidget(ModelForm):
    foreign = ForeignField(to='foreign_fields.Target', selector="char")

    class Meta:
        model = Referrer
        fields = "__all__"

class ForeignFormAreaTestDefaultWidget(ModelForm):
    many = TextAreaToManyField(to='foreign_fields.Target', selector="char")

    class Meta:
        model = Referrer
        fields = "__all__"
