from django.urls import path,include
from api_app import views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version="v1",
        description="API documentation for the Project Management Tool",
    ),
    public=True,
)


# default router
router = DefaultRouter()

# router register
router.register(r'users',views.UsersViewset,basename='user')
router.register(r'projects',views.ProjectsViewset,basename='project')
router.register(r'tasks',views.TasksViewset,basename='task')

urlpatterns = [
    path('',include(router.urls)),
    path('projects/<int:project_id>/tasks/',views.TasksViewset.as_view({'get':'list','post':'create'}), name='project-tasks'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

