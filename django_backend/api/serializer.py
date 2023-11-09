
from django.db.models import fields
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_permissions = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_permissions']
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Person
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectBlog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = CommentBlog
        fields = '__all__'