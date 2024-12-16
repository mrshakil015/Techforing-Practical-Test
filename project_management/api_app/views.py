from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

#---- Users Model Viewsets
class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

#--- Project model viewset
class ProjectsViewset(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    
#---- Task model viewset
class TasksViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if project_id:
            return Tasks.objects.filter(Project_id = project_id)
        return Tasks.objects.all()
 
#---- Comment model viewset   
class CommentsViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        if task_id:
            return Comments.objects.filter(Task_id = task_id)
        return Comments.objects.all()
        