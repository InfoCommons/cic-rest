# Generated by Django 3.2.8 on 2021-10-28 16:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ror', models.CharField(blank=True, max_length=1000)),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=1000)),
                ('state', models.CharField(blank=True, max_length=1000)),
                ('zip', models.CharField(blank=True, max_length=1000)),
                ('country', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=1000)),
                ('last_name', models.CharField(blank=True, max_length=1000)),
                ('orcid', models.CharField(blank=True, max_length=1000)),
                ('emails', models.CharField(blank=True, max_length=1000)),
                ('private_emails', models.CharField(blank=True, max_length=1000)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None)),
                ('affiliations', models.ManyToManyField(blank=True, null=True, to='apis.Organization')),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]