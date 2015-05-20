from django.forms import ModelForm
from projects.models import Project
from projects.models import Tag
from hubusers.models import HubUser
from django import forms
import datetime

# Create your models here.
class ProjectForm(forms.ModelForm):
    github_password = forms.CharField(widget = forms.PasswordInput, max_length = 30)
    class Meta:
        model = Project
        fields = ['name', 'github_password', 'owners', 'descript', 'language', 'status', 'version', 'icon', ]
        created_on = datetime.datetime.now()
        widgets = {
            'github_password': forms.PasswordInput(),
        }
class TagForm(ModelForm):
    model = Tag
    fields = [Tag]
    