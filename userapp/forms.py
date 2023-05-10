from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'
    #
    # def clean_year_of_birth(self):
    #     year_of_birth = self.cleaned_data['year_of_birth']
    #     if year_of_birth < 1900:
    #         raise forms.ValidationError("Must be older than 1900.")
    #     return year_of_birth


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

