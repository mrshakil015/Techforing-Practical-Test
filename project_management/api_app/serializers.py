from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','email','password','first_name','last_name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ['Created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        exclude = ['Created_at']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ['Created_at']