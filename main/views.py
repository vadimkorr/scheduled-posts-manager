from django.shortcuts import render
from django.http import HttpResponse
from services.db.posts import getPost


def posts(request):
    return render(request, 'posts.html')


def post(request, id):
    post = getPost(id)
    ctx = {"post": post}
    return render(request, 'post.html', context=ctx)


def schedule(request):
    return render(request, 'schedule.html')
