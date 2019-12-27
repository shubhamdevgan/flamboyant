from django.shortcuts import render
from django import views
from .forms import project_form
from django.shortcuts import render,redirect,HttpResponse
from apps.profiles.models import profiles,User
from django.contrib import messages
from .models import projects
from apps.notification.models import *


class Add_project(views.View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            loggeduser=profiles.objects.get(Username__username=request.user)
            notifications=notification.objects.filter(user__Username__username=request.user)
            

            return render(
                request,
                'AddProject.html',
                context={
                    'notification':notifications,
                    'form': project_form(initial={"by_username":loggeduser})
                }
            )
        else:
            messages.success(request,'You are not authorised to access the page you requested,Please Login first')
            return redirect('profiles:Login')


    def post(self,request,*args,**kwargs):
        form=project_form(request.POST)
        if form.is_valid():
            form.save()
            msg="Project "+request.POST['project_name']+" Was added successfully"
            messages.success(request,msg)
            return redirect('projects:ProjectList')
           # projects.objects.get(by_username__username=request.user)
        
        else:
            return HttpResponse(
                '''
                <html><body><h1>Not valid'''
                )

def AllProjects(request):
    All_projects=projects.objects.all()
    notifications=notification.objects.filter(user__Username__username=request.user)
        

    return render(
        request,
        'project_final.html',
        context={
            'notification':notifications,

            'project_list':All_projects
        }
    )


def project_list(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(username=request.user.username)
        project_by_user=current_user.projects.all()
        notifications=notification.objects.filter(user__Username__username=request.user)

        return render(
            request,
            'Project_List.html',
            context={
                'notification':notifications,
                'project_list':project_by_user
            }
        )
    else:
        messages.success(request,'You are not authorised to access the page you requested,Please Login first')
        return redirect('profiles:Login')

def project_detail(request,Pid):
    Project_detail=projects.objects.get(id=Pid)
    notifications=notification.objects.filter(user__Username__username=request.user)
    response = render(
        request,
        'ProjectDetails.html',
        context={
            'notification':notifications,

            'Project_detail':Project_detail
        }
    ) 
    response.set_cookie(key='project', value=Project_detail.id) #setting cookie so it can be used,
    return response                                             #to identify which project to edit
    #return render(
    #    request,
    #    
    #)

class Edit_project(views.View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            project_id = request.COOKIES['project'] #get project id from cookie,so we can know which project to edit
            loggeduser=profiles.objects.get(Username__username=request.user)
            return render(
                request,
                'form1.html',
                context={
                'form': project_form(initial={"by_username":loggeduser},instance=projects.objects.get(id=project_id))
                }
            )
        else:
            messages.success(request,'You are not authorised to access the page you requested,Please Login first')
            return redirect('profiles:Login')

    def post(self,request,*args,**kwargs):
        project_id = request.COOKIES['project']
        form=project_form(request.POST,instance=projects.objects.get(id=project_id))
        if form.is_valid():
            form.save()
            messages.success(request,('Project saved successfully'))
            return redirect('projects:EditProject')
           # projects.objects.get(by_username__username=request.user)
        
        else:
            return HttpResponse(
                '''
                <html><body><h1>Not valid'''
                )

def Delete_project(request):
    some_var=request.POST.getlist('checks[]')
    print("printing project Id's")
    print(some_var)
    for x in some_var:
        y=projects.objects.get(id=x)
        y.delete()

    return redirect('projects:ProjectList')