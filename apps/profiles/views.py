from django.shortcuts import render,redirect,HttpResponse

from django import views
from .models import profiles,User
from .forms import LoginForm,ProfileForm,RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.notification.models import *

def HomeView(request):
    return render(
        request,
        'index.html',
        
    )

class LoginView(views.View):
    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(
            request,
            'Login.html',
            context={
            'form':form    
            }
        )
    
    def post(self,request,*args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles:profile')
        else:
            return render(
                request,
                'Login.html',
                context={
                    'form':LoginForm(),
                    'error':'Incorrect Username or password',
                }
            )

def LogoutView(request):
    logout(request)
    return redirect(
    'profiles:Login'
    )

def DeleteProfile(request):
    profile=User.objects.get(username=request.user.username)
    profile.delete()
    return redirect('profiles:Login')


class RegisterView(views.View):
    def get(self,request,*args, **kwargs):
        form=RegisterForm
        return render(
            request,
            'Registeration.html',
            context={
            'form':form    
            }
        )

    def post(self,request,*args, **kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'])
            user = authenticate(request,username=request.POST['username'],password=request.POST['password1'])
            login(request,user)
            return redirect('profiles:Editprofile')
        else:
            return render(
            request,
            'Registeration.html',
            context={
            'form':form,
            'error':form.non_field_errors
            }
            )

#@login_required(login_url='http://127.0.0.1:8000/profiles/login/')
def ProfileView(request,*args, **kwargs): 

    if request.user.is_authenticated:
        profile=profiles.objects.get(Username__username=request.user)
        previous_projects=profile.previous_projects
        previous_projects_list = []
        notifications=notification.objects.filter(user__Username__username=request.user)
        
        if previous_projects:
            for x in previous_projects.split(','):
                previous_projects_list.append(x)
        print(previous_projects_list)
        return render(
        request,
        'UserProfile.html',
        context={
            'notification':notifications,
            'previous_projects':previous_projects_list,
            'profile':profile
        }
        ) 
        '''previouly used return redirect('profiles:profile') but it caused an loop
           #doubt in this ,will this work  properly in future
        '''
    else:
        messages.success(request,('You must Login into system for access'))
        return redirect('profiles:Login')
        
        '''
        when submiting using this render form profile doesn't redirect to
        profile page
        previously used this :
        return render(
        request,
        'login.html',
        context={
            'form':LoginForm(),
            'error': 'login into system first',
            }
        )
        
        '''

class ProfileEditView(views.View):
    def get(self,request,*args,**kwargs):
        user1=User.objects.get(username=request.user.username)
        if request.user.is_authenticated:
            return render(
            request,
            'ProfileUpdate.html',
            context={
            'form':ProfileForm(instance =request.user.profile)
            }
            ) 
            
        else:
            messages.success(request,('You must Login into system for access'))
            return redirect('profiles:Login')

    def post(self,request,*args,**kwargs):
        user=User.objects.get(username=request.user.username)
        print(user)
        form=ProfileForm(data=request.POST,files=request.FILES,instance =user) #what is use of instance here
        if form.is_valid():
            # profile is valid now bring profile instance
            profile = profiles.objects.get(Username=user)
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name= form.cleaned_data['last_name']
            profile.email_id= form.cleaned_data['email_id']
            profile.experience= form.cleaned_data['experience']
            profile.previous_projects= form.cleaned_data['previous_projects']
            profile.user_type= form.cleaned_data['user_type']
            profile.profile_dp=form.cleaned_data['profile_dp']
            profile.save()
            form.save()
            messages.success(request,('Profile Edited succesfully'))
            return redirect('profiles:profile')


def UserProfile(Pid,request):
    profile=profiles.object.get(id=Pid)
    return render(
        request,
        'profile1.html',
        context={
            'profile':profile
        }
    )

class tryv(views.View):
    def get(self,request,*args, **kwargs):
        return render(
            request,
            'Login.html'
        )
    
    def post(self,request,*args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles:profile')
        else:
            return render(
                request,
                'index1.html',
                context={
                    'error':'Incorrect Username or password',
                }
            )
