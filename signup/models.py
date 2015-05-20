from django.db import models
from django import forms

# Create your models here.
class UserForm(forms.Form):
    name = froms.CharField(max_length = 100)
    email = forms.EmailField()
    username = forms.CharField(max_length = 50)
    password = forms.CharField(min_length = 6, max_length = 25)
    passval = forms.charfield(min_length = 6, max_length = 25)
    