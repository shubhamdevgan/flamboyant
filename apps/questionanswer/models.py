from django.db import models
from apps.profiles.models import *
from apps.projects.models import *
from apps.exam.models import *
from apps.marks.models import *
from apps.questions.models import *

class questionanswer(models.Model):

    que=models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        related_name='Questions'
    )

    answered=models.BooleanField(
        default=False
    )

    by_user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='by_username'
    )

    exam=models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='exam',
        null=True,
        blank=True
    )

    marks=models.ForeignKey(
        Marks,
        on_delete=models.CASCADE,
        related_name='marks',
        null=True,
        blank=True
    )