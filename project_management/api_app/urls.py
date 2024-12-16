from django.urls import path,include
from api_app import views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version="v1",
        description="API documentation for the Project Management Tool",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


# default router
router = DefaultRouter()

# router register
router.register(r'users',views.UserViewSet,basename='user')
router.register(r'projects',views.ProjectsViewset,basename='project')
router.register(r'tasks',views.TasksViewset,basename='task')
router.register(r'comments',views.CommentsViewset,basename='comment')

urlpatterns = [
    path('',include(router.urls)),
    path('users/register/', views.UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('users/login/', views.UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('projects/<int:project_id>/tasks/',views.TasksViewset.as_view({'get':'list','post':'create'}), name='project-tasks'),
    path('tasks/<int:project_id>/comments/',views.CommentsViewset.as_view({'get':'list','post':'create'}), name='task-comments'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

