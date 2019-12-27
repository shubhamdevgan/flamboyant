from django.db import models
from apps.profiles.models import *
class notification(models.Model):
    
    user=models.ForeignKey(
        profiles,
        on_delete=models.CASCADE,
        related_name='notification'
    )

    notification_content=models.CharField(
        max_length=150
    )

    time_stamp=models.DateTimeField(
        auto_now_add=True
    )

    status=models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.user.Username.username