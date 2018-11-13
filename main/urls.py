from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/<int:id>/', views.hello, name='hello'),
]
