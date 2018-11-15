from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:id>', views.post, name='post'),
    path('schedule', views.schedule, name='schedule'),
]
