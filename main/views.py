from django.shortcuts import render
from django.http import HttpResponse


def posts(request):
    return render(request, 'main/posts.html')


def post(request, id):
    return render(request, 'main/post.html')


def schedule(request):
    return render(request, 'main/schedule.html')
