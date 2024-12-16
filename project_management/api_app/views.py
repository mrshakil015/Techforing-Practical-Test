from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

# Users Model Viewsets
class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class ProjectsViewset(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    
class TasksViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if project_id:
            return Tasks.objects.filter(Project_id = project_id)
        return Tasks.objects.all()
        