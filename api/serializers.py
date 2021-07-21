from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Note, Summary


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__' 

class SummarySerializer(ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__' 
