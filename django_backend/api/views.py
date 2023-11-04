from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets, permissions

class AboutMeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY
