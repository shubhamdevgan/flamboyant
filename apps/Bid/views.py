from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django import views
from apps.projects.models import *
from apps.notification.models import *
from apps.notification.models import *
from apps.marks.models import *


class DoBid(views.View):
    def get(self,request,*args,**kwargs):
        notifications=notification.objects.filter(user__Username__username=request.user)        
        loggeduser=profiles.objects.get(Username__username=request.user)
        on_project=projects.objects.get(id=kwargs['Pid'])
        return render(
                    request,
                    'form4.html',
                    context={
                        'notification':notifications,
                        'form': BidForm(initial={"by_user":loggeduser,"on_project":on_project})
                    }
                )

    def post(self,request,*args,**kwargs):
        loggeduser=profiles.objects.get(Username__username=request.user)
        on_project=projects.objects.get(id=kwargs['Pid'])
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:AllProjects')

        else:
            return render(
                    request,
                    'form4.html',
                    context={
                        'error':'TRy AGAIN',
                        'form': BidForm(initial={"by_username":loggeduser})
                    }
                )

def ViewBid(request,Xid):
    bids=Bid.objects.filter(on_project=Xid)
    notifications=notification.objects.filter(user__Username__username=request.user)
    return render(
        request,
        'BidsOnProject.htm',
        context={
            'notification':notifications,
            'bids':bids
        }
    )

def BidDetail(request,BId):
    notifications=notification.objects.filter(user__Username__username=request.user)
    print('Bid ID is',BId)
    bid=Bid.objects.filter(id=BId)
    print(bid[0].by_user)
    mark=Marks.objects.filter(on_project=bid[0].on_project,by_user__username=bid[0].by_user.Username)
    print(mark)
    marks=0
    for x in range(0,len(mark)):
        marks=marks+mark[x].marks_scored

    print(marks)
    return render(
        request,
        'BidDetail.html',
        context={
            'marks':marks,
           'notification':notifications,

            'bid':bid
        }
    )
    
def AcceptBid(request):
    notifications=notification.objects.filter(user__Username__username=request.user)
    BidId=int(request.POST['BID'])
    Selected_Bid=Bid.objects.get(id=BidId)
    Selected_Bid.status=True
    Selected_Bid.save()
    content=Selected_Bid.on_project.project_name
    Con_final='Your Bid On Project '+content+' is accepted'
    notification.objects.create(
        user=Selected_Bid.by_user,
        notification_content=Con_final)
    
    other_users=Bid.objects.filter(on_project=Selected_Bid.on_project,status=False)
    Con_final='Your Bid On Project '+content+' is Rejected'

    for x in other_users:
        notification.objects.create(
        user=x.by_user,
        notification_content=Con_final)
    
    return redirect('projects:ProjectList')
    