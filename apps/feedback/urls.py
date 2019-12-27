from django.urls import path
from .views import Writefeedback
urlpatterns = [
    path('Writefeedback/',Writefeedback.as_view(),name='WriteFeedback'),
  
]

