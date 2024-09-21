from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    salary = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Name: {self.name} Age: {self.age}, Instrument: {self.instrument}, Salary: {self.salary}"

