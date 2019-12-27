from django.db import models

from apps.profiles.models import *
# Create your models here.
class Wallet(models.Model):
    
    username=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='wallet'
        )

    money=models.IntegerField(
        verbose_name='Amount'
        )
    
    def __str__(self):
        return self.username
