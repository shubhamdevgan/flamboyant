from django.shortcuts import render
from django import views

def CheckAnswers(request):
    user=request.user
    
    if request.POST.getlist['checkbox']== 4:
        pass