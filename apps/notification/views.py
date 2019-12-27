from django.shortcuts import render
from .models import *

def ViewNotificatons(request):
    pass

def ChangeStatus(request):
    print('called')
    notifications=notification.objects.filter(user__Username__username=request.user,status=False)

    for x in notifications:
        x.status=True
        x.save()

        