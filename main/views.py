from django.shortcuts import render
from django.http import HttpResponse


def hello(request, id):
    text = "<h1>Welcome to the app; id: %s</h1>" % id
    return HttpResponse(text)

# Create your views here.
