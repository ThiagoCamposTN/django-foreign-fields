=====================
Django Foreign Fields
=====================

.. image:: https://img.shields.io/pypi/v/django-foreign-fields.svg
   :target: https://pypi.python.org/pypi/django-foreign-fields
   :alt: PyPI

Django Foreign Fields is a Django app that offers two new form fields that help handling foreign relationships in a easier way.

Quick start
-----------
.. code:: bash

   $ pip install django-foreign-fields

Usage
-----
Django-foreign-fields adds two new form fields ``ForeignField`` and ``TextAreaToManyField``.

Fields
^^^^^^
Both form fields need two new arguments: ``to`` and ``selector``.

* ``to``: the `target` model of the relationship. Declaring the `target` model as the first parameter will automatically be detected as the `to` argument.

* ``selector``: the model field where the given value will be searched on.

ForeignField
""""""""""""
Receives data and searches for an object in database that has that unique value on the given field. The object is stored as a ``ForeignKey``.

TextAreaToManyField
"""""""""""""""""""
Breaks all lines in a ``Textarea`` and use each one to find objects that correspond to each search. Each search must return a unique object, then, all objects are stored in a ``ManyToMany`` relationship.

Examples
^^^^^^^^
ForeignField
""""""""""""
Given you already have two models, one ``Target`` that holds some information and one ``Referrer`` that will make a foreign relationship to a particular field:

.. code:: python

   class Target(models.Model):
      name = models.TextField()

   class Referrer(models.Model):
      foreign = models.ForeignKey()

It will be needed a new form for the ``Referrer``.

The original form field that holds the foreign key relation on the ``Referrer`` will be substituted for the ``ForeignField``:

.. code:: python

   import foreign_fields.ForeignField

   class ReferrerForm(forms.ModelForm):
      foreign = foreign_fields.ForeignField(to=Target, selector='name')
      
      class Meta:
           model = Referrer

Now you can use the form on your ``View``. The default widget is ``TextInput``, so when you enter a string in the field and save the form, the ``ForeignField`` will search for a ``Target`` that has the given string in it's ``name`` field that must be unique. If the field is not unique, it will be given a ``ValidationError``.

It's possible to change the foreign widget into others such as ``NumberInput`` or ``DateInput``.

TextAreaToManyField
""""""""""""
Given you already have two models, one ``Target`` that holds some information and one ``Referrer`` that will make a many to many relationship to a particular field:

.. code:: python

   class Target(models.Model):
      name = models.TextField()

   class Referrer(models.Model):
      many_to_many = models.ManyToManyField()

It will be needed a new form for the ``Referrer``.

The original form field that holds the many to many relation on the ``Referrer`` will be substituted for the ``TextAreaToManyField``:

.. code:: python

   import foreign_fields.TextAreaToManyField

   class ReferrerForm(forms.ModelForm):
      many_to_many = foreign_fields.TextAreaToManyField(to=Target, selector='name')
      
      class Meta:
           model = Referrer

Now you can use the form on your `View`. The default widget is ``Textarea``, so when you enter a text in the field and save the form, the ``TextAreaToManyField`` will split each line and search for a unique ``Target`` by line that has the given string in it's `name` field. If the field is not unique, it will be given a `ValidationError`.
