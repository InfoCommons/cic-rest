from django.db import models
from django.contrib.postgres.fields import ArrayField


class Organization(models.Model):
    class Meta:
        db_table = 'organization'

    id = models.IntegerField(primary_key=True)
    ror = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=1000, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=1000, blank=True)
    state = models.CharField(max_length=1000, blank=True)
    zip = models.CharField(max_length=1000, blank=True)
    country = models.CharField(max_length=1000, blank=True)


class Person(models.Model):
    class Meta:
        db_table = 'person'

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=1000, blank=True)
    last_name = models.CharField(max_length=1000, blank=True)
    orcid = models.CharField(max_length=1000, blank=True)
    emails = models.CharField(max_length=1000, blank=True)
    private_emails = models.CharField(max_length=1000, blank=True)
    keywords = ArrayField(models.CharField(max_length=100, blank=True))
    affiliations = models.ManyToManyField('Organization', blank=True, null=True)
