from django.urls import path
from . import views


urlpatterns = [
    path('register', views._register, name='register'),
    path('logout', views._logout, name='logout'),
    path('login', views._login, name='login'),
]
