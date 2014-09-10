
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Violation(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.TextField(blank=True)
    product = models.TextField(blank=True)
    invalid = models.TextField(blank=True)
    execution = models.TextField(blank=True)
    address = models.TextField(blank=True)
    location = models.TextField(blank=True)
    date = models.TextField(blank=True)
    timestamp = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'violation'

