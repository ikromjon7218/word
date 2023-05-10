from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Profil(models.Model):
    G = [('male', 'male'),
         ('female', 'female')]
    name = models.CharField(max_length=50)                       # full name
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # username, password
    gender = models.CharField(max_length=7, choices=G)

    tel_number = models.CharField(max_length=20, null=True, blank=True)   # contact
    year_of_birth = models.PositiveSmallIntegerField()                    # for example: 2007

    test = models.PositiveIntegerField(default=0)               # Number of tests
    acceptance = models.PositiveIntegerField(default=0)         # The number of correct choices
    rejection = models.PositiveIntegerField(default=0)          # Number of incorrect selections
    percentage = models.PositiveSmallIntegerField(default=100)  # Percentage of correct choices, in a 100-point system

    # def clean(self):
    #     if self.year_of_birth < 1900:
    #         raise ValidationError("Must be older than 1900.")

    def __str__(self):
        return self.name
