from django.db import models
from apps.projects.models import *
from apps.profiles.models import *

class feedback(models.Model):
    on_user=models.ForeignKey(
        User,
        on_delete='Models.Cascade',
        related_name='feedback'
    )

    by_user=models.ForeignKey(
        User,
        on_delete='models.cascade',
        related_name='by_user'
    )

    feedback_text=models.TextField(
        
    )