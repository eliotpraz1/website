
from django.db.models import fields
from .models import *
from rest_framework import serializers
 
class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'