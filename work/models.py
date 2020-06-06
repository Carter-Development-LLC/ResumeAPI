from datetime import date
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from tinymce.models import HTMLField
from bs4 import BeautifulSoup


def max_value_validator_current_year(value):
    MaxValueValidator(date.today().year)(value)


class Job(models.Model):
    class Month(models.IntegerChoices):
        JANUARY = 1, 'Jan'
        FEBRUARY = 2, 'Feb'
        MARCH = 3, 'Mar'
        APRIL = 4, 'Apr'
        MAY = 5, 'May'
        JUNE = 6, 'Jun'
        JULY = 7, 'Jul'
        AUGUST = 8, 'Aug'
        SEPTEMBER = 9, 'Sep'
        OCTOBER = 10, 'Oct'
        NOVEMBER = 11, 'Nov'
        DECEMBER = 12, 'Dec'

    id = models.UUIDField(default=uuid4, editable=False,
                          primary_key=True, unique=True)
    company = models.CharField(max_length=100)
    currently_employed = models.BooleanField()
    description = HTMLField()
    end_month = models.IntegerField(
        blank=True, choices=Month.choices, null=True)
    end_year = models.IntegerField(blank=True, null=True, validators=[
                                   MinValueValidator(2015), max_value_validator_current_year])
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=2)
    position = models.CharField(max_length=100)
    start_month = models.IntegerField(choices=Month.choices)
    start_year = models.IntegerField(
        validators=[MinValueValidator(2015), max_value_validator_current_year])

    def __str__(self):
        return self.company + ' - ' + self.position

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.description = "".join(self.description.splitlines())

        soup = BeautifulSoup(self.description)
        links = soup.find_all('a')
        for link in links:
            link['class'] = ['external-link']
            link['rel'] = ['noopener', 'noreferrer']

        self.description = str(soup)

        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)
