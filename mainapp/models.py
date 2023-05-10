from django.db import models
from userapp.models import Profil
# from django.contrib.postgres.fields import ArrayField

class Book(models.Model):
    name = models.CharField(max_length=32)      # full name
    about = models.CharField(max_length=1000)   # about the book
    def __str__(self):
        return self.name

class Word(models.Model):
    name = models.CharField(max_length=35)                      # full name
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    unit = models.PositiveSmallIntegerField()         # Unit number
    def __str__(self):
        return self.name

class Soz(models.Model):
    name = models.CharField(max_length=35)                      # full name
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Amount(models.Model):
    amount_number = models.PositiveSmallIntegerField(default=1)
    amount = models.PositiveSmallIntegerField(default=2)
    from_unit = models.PositiveSmallIntegerField(default=1)
    to_unit = models.PositiveSmallIntegerField(default=2)
    language = models.CharField(max_length=10, default="eng-uzb")
    acceptance = models.PositiveSmallIntegerField(default=0)
    question_soz = models.PositiveIntegerField(default=1)
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE, default=1)
    # error = ArrayField(models.PositiveSmallIntegerField(), null=True)
    def __str__(self):
        return f"{self.amount_number} / {self.amount}"
