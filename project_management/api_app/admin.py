from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(ProjectMember)
admin.site.register(Tasks)
admin.site.register(Comments)