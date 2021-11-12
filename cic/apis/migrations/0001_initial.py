# Generated by Django 3.2.8 on 2021-11-12 19:31

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funder',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ror', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'funder',
            },
        ),
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
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('orcid', models.CharField(blank=True, max_length=255, null=True)),
                ('emails', models.CharField(blank=True, max_length=255, null=True)),
                ('private_emails', models.CharField(blank=True, max_length=255, null=True)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None)),
                ('affiliations', models.ManyToManyField(blank=True, to='apis.Organization')),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('award_id', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('funder_divisions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), blank=True, default=list, size=None)),
                ('program_reference_codes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), blank=True, default=list, size=None)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('award_amount', models.IntegerField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None)),
                ('awardee_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.organization')),
                ('funder', models.ForeignKey(blank=True, db_column='funder', null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.funder')),
                ('other_investigators', models.ManyToManyField(blank=True, related_name='grant_other_investigators', to='apis.Person')),
                ('principal_investigator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grant_pi', to='apis.person')),
                ('program_officials', models.ManyToManyField(blank=True, to='apis.Person')),
            ],
            options={
                'db_table': 'grant',
            },
        ),
    ]
