from django.db import models
from apps.wallet.models import *
from apps.profiles.models import *
class Transactions(models.Model):
    
    #What if We want to keep Transactions OF an User

    of_wallet=models.ForeignKey(
        Wallet,
        on_delete='models.CASCADE',
        related_name='transactions',

    )

    Transaction_id=models.AutoField(
        primary_key=True
    )

    from_user=models.OneToOneField(
        User,
        on_delete='None',
        related_name='from_user'
    )

    to_user=models.OneToOneField(
        User,
        on_delete='None',
        related_name='to_user'
    )

    Transaction_date=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Transaction Done on'
    )

    amount=models.IntegerField(
        verbose_name='Amount Transferred'
    )