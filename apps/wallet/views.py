from django.shortcuts import render
from .models import *
# Create your views here.
def walletView(request):
    if request.user.is_authenticated:
        pass