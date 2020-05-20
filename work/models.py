from datetime import date
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from tinymce.models import HTMLField

def max_value_validator_current_year(value):
    MaxValueValidator(date.today().year)(value)

class Job(models.Model):
    class Month(models.IntegerChoices):
        JANUARY = 1, 'January'
        FEBRUARY = 2, 'February'
        MARCH = 3, 'March'
        APRIL = 4, 'April'
        MAY = 5, 'May'
        JUNE = 6, 'June'
        JULY = 7, 'July'
        AUGUST = 8, 'August'
        SEPTEMBER = 9, 'September'
        OCTOBER = 10, 'October'
        NOVEMBER = 11, 'November'
        DECEMBER = 12, 'December'

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)
    company = models.CharField(max_length=100)
    currently_employed = models.BooleanField()
    description = HTMLField()
    end_month = models.IntegerField(blank=True, choices=Month.choices, null=True)
    end_year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(2015), max_value_validator_current_year])
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=2)
    position = models.CharField(max_length=100)
    start_month = models.IntegerField(choices=Month.choices)
    start_year = models.IntegerField(validators=[MinValueValidator(2015), max_value_validator_current_year])

    def __str__(self):
        return self.company + ' - ' + self.position

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.description = "".join(self.description.splitlines())
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
