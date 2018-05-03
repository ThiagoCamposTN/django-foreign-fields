from django.test import TestCase

from .test_forms import (ForeignFormAreaTestDefaultWidget,
                         ForeignFormTestDateTime, ForeignFormTestDefaultWidget,
                         ForeignFormTestInteger)
from .test_models import Target


class ForeignFieldTestCase(TestCase):
    def setUp(self):
        self.target_one = Target.objects.create(integer=1, datetimenew='2007-10-10', char='test')

    def test_foreign_form_is_valid(self):
        data = {'foreign': '2007-10-10'}

        form = ForeignFormTestDateTime(data)

        self.assertTrue(form.is_valid())

    def test_foreign_datetime_reference_is_valid(self):
        data = {'foreign': '2007-10-10'}

        form = ForeignFormTestDateTime(data)
        foreign_object = form.save()

        self.assertTrue(foreign_object.foreign == self.target_one)

    def test_new_foreign_form_is_valid(self):
        data = {'foreign': '1'}

        form = ForeignFormTestInteger(data)

        self.assertTrue(form.is_valid())

    def test_foreign_integer_reference_is_valid(self):
        data = {'foreign': '1'}

        form = ForeignFormTestInteger(data)
        foreign_object = form.save()

        self.assertTrue(foreign_object.foreign == self.target_one)

    def test_foreign_char_reference_is_valid(self):
        data = {'foreign': 'test'}

        form = ForeignFormTestDefaultWidget(data)
        foreign_object = form.save()

        self.assertTrue(foreign_object.foreign == self.target_one)

class ForeignFieldAreaTestCase(TestCase):
    def setUp(self):
        self.target_one = Target.objects.create(integer=1, datetimenew='2007-10-10', char='test')
        self.target_two = Target.objects.create(integer=2, datetimenew='2011-04-19', char='teste')

    def test_many_form_is_valid(self):
        data = {'many': 'test\nteste'}

        form = ForeignFormAreaTestDefaultWidget(data)

        self.assertTrue(form.is_valid())

    def test_many_char_reference_is_valid(self):
        data = {'many': 'test\nteste'}

        form = ForeignFormAreaTestDefaultWidget(data)
        foreign_object = form.save()

        self.assertTrue(list(foreign_object.many.all()) == [self.target_one, self.target_two])
