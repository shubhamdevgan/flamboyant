from django.urls import path
from .views import DisplayQuestion

urlpatterns = [
    path('que/',DisplayQuestion,name='Que'),
   
]


