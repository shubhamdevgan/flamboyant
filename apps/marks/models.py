from django.db import models
from apps.profiles.models import *
from apps.projects.models import *
from apps.exam.models import *
from apps.questions.models import *

class Marks(models.Model):

    by_user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Marks_by_user'
    )

    marks_scored= models.IntegerField(
        verbose_name='Marks Scored',

    )

    on_project=models.ForeignKey(
        projects,
        on_delete='Nothing',
        related_name='on_project'
    )
