from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAdminUser]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectBlog.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAdminUser]



class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentBlog.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAdminUser]