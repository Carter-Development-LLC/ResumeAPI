# Generated by Django 3.0.6 on 2020-05-20 02:12

import django.core.validators
from django.db import migrations, models
import tinymce.models
import uuid
import work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company', models.CharField(max_length=100)),
                ('currently_employed', models.BooleanField()),
                ('description', tinymce.models.HTMLField()),
                ('end_month', models.IntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True)),
                ('end_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2015), work.models.max_value_validator_current_year])),
                ('location_city', models.CharField(max_length=100)),
                ('location_state', models.CharField(max_length=2)),
                ('position', models.CharField(max_length=100)),
                ('start_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('start_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2015), work.models.max_value_validator_current_year])),
            ],
        ),
    ]
