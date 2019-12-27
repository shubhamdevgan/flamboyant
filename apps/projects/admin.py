from django.contrib import admin
from apps.projects.models import *

# Register your models here.
class projectsadmin(admin.ModelAdmin):
    list_display = ('project_name','by_username',)

admin.site.register(projects,projectsadmin)