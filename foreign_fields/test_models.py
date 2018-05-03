from django.db import models
from django.utils import timezone


class Referrer(models.Model):
    foreign = models.ForeignKey('Target', null=True, blank=True, 
                                on_delete=models.SET_NULL, related_name="foreign_test")
    many    = models.ManyToManyField('Target', blank=True, related_name="many_test")

class Target(models.Model):
    integer     = models.IntegerField()
    datetimenew = models.DateField(default=timezone.now)
    char        = models.TextField(default='')
