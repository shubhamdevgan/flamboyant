from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('notifications/',ViewNotificatons,name='NotificationView'),
    path('changestatus/',ChangeStatus,name='StatusChange')
]
