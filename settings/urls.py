"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django_private_chat import urls as django_private_chat_urls
from apps.profiles.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/',include(('apps.profiles.urls','profiles'))),
    path('projects/',include(('apps.projects.urls','projects'))),
    path('wallet/',include(('apps.wallet.urls','wallet'))),
    path('question/',include(('apps.questions.urls','questions'))),
    path('feedback/',include(('apps.feedback.urls','feedback'))),
    path('bid/',include(('apps.Bid.urls','bid'))),
    path('QA/',include(('apps.questionanswer.urls','QA'))),
    path('', HomeView),
    path('notification/',include(('apps.notification.urls','notification')))
   # path('transactions/',include(('apps.Transactions.urls','transaction')))
]
