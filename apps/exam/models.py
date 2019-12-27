from django.db import models
from django.contrib.auth.models import User
from  apps.projects.models import *
class Exam(models.Model):

    exam_id=models.AutoField(primary_key=True)

    by_user=models.ForeignKey(    
        User,
        on_delete=models.CASCADE,
        related_name='exams'
    )
    
    on_project=models.ForeignKey(
        projects,
        on_delete=models.CASCADE,
        related_name='exam_on_project',
        null=True
    )

    def __str__(self):
        return self.on_project.project_name
