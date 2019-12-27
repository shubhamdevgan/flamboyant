from django.urls import path

from .views import LoginView,RegisterView,LogoutView,ProfileView,tryv,ProfileEditView,DeleteProfile,UserProfile
from .views import HomeView


urlpatterns = [
    path('login/',LoginView.as_view(),name='Login'),
    path('register/',RegisterView.as_view(),name='Register'),
    path('logout/',LogoutView,name='Logout'),
    path('profile/',ProfileView,name='profile'),
    path('editprofile',ProfileEditView.as_view(),name='Editprofile'),
    path('try/',tryv.as_view(),name='tryv'),
    path('delete_profile/',DeleteProfile,name='DeleteProfile'),
    path('userprofile/<int:Pid>',UserProfile,name='UserProfile'),
    path('home/',HomeView,name='Home')
]

