from datetime import date
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

def max_value_validator_current_year(value):
    MaxValueValidator(date.today().year)(value)

class School(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)
    city = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    gpa = models.DecimalField(decimal_places=2, max_digits=3)
    graduated = models.BooleanField()
    graduation_date = models.DateField(null=True)
    major = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name + ' - ' + self.degree

class Course(models.Model):
    class Semester(models.IntegerChoices):
        FALL = 1, 'Fall'
        WINTER = 2, 'Winter'
        SPRING = 3, 'Spring'
        SUMMER = 4, 'Summer'

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    description = models.TextField()
    featured = models.BooleanField()
    name = models.CharField(max_length=100)
    semester = models.IntegerField(choices=Semester.choices)
    stub = models.CharField(max_length=10, unique=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2015), max_value_validator_current_year])

    def __str__(self):
        return self.stub
