from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('new', views.newPost, name='newPost'),
    path('<str:id>', views.post, name='post'),
]
