from django.urls import path
from .views import *

urlpatterns = [
    path('wallet/',walletView,name='walletHome')
]