from django.db import models
from userapp.models import Profil

class Memorization(models.Model):
    question_lar = models.CharField(max_length=3010, default="[]")
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE)
    book = models.PositiveSmallIntegerField(default=1)
    unit = models.PositiveSmallIntegerField(default=3)
    language = models.CharField(max_length=10, default="eng-uzb")

    def __str__(self):
        return f"{self.profil.name} {self.book}"
