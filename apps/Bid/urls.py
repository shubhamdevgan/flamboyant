from django.urls import path
from .views import *

urlpatterns = [
    path('bid/<int:Pid>',DoBid.as_view(),name='MakeBid'),
    path('viewbid/<int:Xid>',ViewBid,name='ViewBids'),
    path('acceptbid/',AcceptBid,name='AcceptBid'),
    path('bidDetail/<int:BId>',BidDetail,name='BidDetail')
  
]

