from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','password','first_name','last_name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'