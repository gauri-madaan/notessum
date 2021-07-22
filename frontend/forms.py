from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from api.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        # widget = {
        #     'body': forms.TextInput(attrs={'class'})
        # }