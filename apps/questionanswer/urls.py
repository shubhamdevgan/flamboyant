from django.urls import path
from .views import *

urlpatterns = [
    path('give_exam/',CheckAnswer.as_view(),name='GiveExam'),
   
]


