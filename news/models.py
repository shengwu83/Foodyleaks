
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



class LocationViolation(models.Model):
    location = models.TextField(blank=True)
    products = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'location_violation'

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    district = models.TextField(blank=True)
    tag = models.TextField(blank=True)
    link = models.TextField(blank=True)
    timestamp = models.IntegerField(blank=True, null=True)
    media = models.TextField(blank=True)
    date = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'news'

class PesticideVegatable(models.Model):
    product = models.TextField()
    year = models.TextField()
    month = models.TextField()
    invalid = models.TextField()
    ppm = models.TextField()
    admin = models.TextField()
    location = models.TextField()
    address = models.TextField()
    execution = models.TextField()
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'pesticide_vegatable'

class Violation(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.TextField(blank=True)
    product = models.TextField(blank=True)
    invalid = models.TextField(blank=True)
    execution = models.TextField(blank=True)
    address = models.TextField(blank=True)
    location = models.TextField(blank=True)
    date = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'violation'

