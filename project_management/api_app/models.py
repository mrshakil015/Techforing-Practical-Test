from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Projects(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Description = models.TextField(null=True)
    Owner = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    Created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.Name
    
class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin','Admin'),
        ('Member','Member'),
    ]
    Project = models.CharField(max_length=100, null=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    Role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
    
    def __str__(self):
        return self.User

class Tasks(models.Model):
    STATUS_CHOICES = [
        ('To Do','To Do'),
        ('In Progress','In Progress'),
        ('Done','Done'),
    ]
    PRIORITY_CHOICES = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]
    
    Title = models.CharField(max_length=100, null=True)
    Description = models.TextField(null=True)
    Status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=True)
    Priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True)
    Assigned_to = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    Project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)
    Due_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.Title

class Comments(models.Model):
    Content = models.TextField(null=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    Task = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)
