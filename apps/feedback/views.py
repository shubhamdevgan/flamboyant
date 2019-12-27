from django.shortcuts import render
from apps.profiles.models import *
from .forms import feedbackForm
from django import views
class Writefeedback(views.View):
    def get(self,request,*args,**kwargs):
        loggeduser=profiles.objects.get(Username__username=request.user)
        return render(
                    request,
                    'form3.html',
                    context={
                        'form': feedbackForm(initial={"by_user":loggeduser})
                    }
                )

    def post(self,request,*args,**kwargs):
        loggeduser=profiles.objects.get(Username__username=request.user)
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                    request,
                    'form3.html',
                    context={
                        'error':'Feedback ADDED succesfully',
                        'form': feedbackForm(initial={"by_user":loggeduser}),
                    }
                )

        else:
            return render(
                    request,
                    'form3.html',
                    context={
                        'error':'TRy AGAIN',
                        'form': feedbackForm(initial={"by_username":loggeduser})
                    }
                )

