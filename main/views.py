from django.shortcuts import render
from django.http import HttpResponse


def posts(request):
    return render(request, 'posts.html')


def post(request, id):
    post = {"id": id}
    ctx = {"post": post}
    return render(request, 'post.html', context=ctx)


def schedule(request):
    return render(request, 'schedule.html')
