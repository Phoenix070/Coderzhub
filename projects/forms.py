from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django import forms
from projects.models import *

from tinymce.widgets import TinyMCE

from django.forms.formsets import formset_factory


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('topic','content')
        widgets = {
            'content': TinyMCE(attrs={'cols': 20, 'rows': 10, 'class':'comment_text'}),
        }

class CommentForm(forms.ModelForm):
    content1 = forms.CharField(widget=TinyMCE(attrs={'cols': 20, 'rows': 20, 'class':'comment_text'}))
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': TinyMCE(attrs={'cols': 20, 'rows': 10, 'class':'comment_text'}),
        }

        
CommentFormSet = formset_factory(CommentForm)