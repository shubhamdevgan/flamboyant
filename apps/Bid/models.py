from django.db import models
from apps.projects.models import *
from apps.profiles.models import *

class Bid(models.Model):
    on_project=models.ForeignKey(
        projects,
        on_delete='models.CASCADE',
        related_name='Bids'
    )
    
    by_user=models.ForeignKey(
        profiles,
        on_delete='models.CASCADE',
        related_name='bid_by_user'
    )

    bid_amount=models.IntegerField(
        verbose_name='Bid Amount'
    )

    status=models.BooleanField(
        default=False
    )