from django import forms
from django.utils import timezone

from .models import Posts

class PostForm(forms.ModelForm):
    #date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
    class Meta:
        model=Posts
        fields=[
            'title',
            'content',
            'post_author',
            #'date',
        ]