from django.urls import path
from .views import Add_project,project_list,project_detail,Edit_project,Delete_project,AllProjects
urlpatterns = [
    path('addproject/',Add_project.as_view(),name='AddProject'),
    path('projectslist/',project_list,name='ProjectList'),
    path('project_detail/<int:Pid>',project_detail,name='ProjectDetail'),
    path('edit_project/',Edit_project.as_view(),name='EditProject'),
    path('project_delete/',Delete_project,name='ProjectDelete'),
    path('projects/',AllProjects,name='AllProjects')
]


