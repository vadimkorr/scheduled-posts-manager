from django.shortcuts import render
from django.http import HttpResponse
from services.db.posts import getPost
from services.db.posts import getPosts
from services.db.posts import putPost


def posts(request):
    posts = getPosts()
    ctx = {"posts": posts}
    return render(request, 'posts.html', context=ctx)


def post(request, id):
    post = getPost(id)
    ctx = {"post": post}
    return render(request, 'post.html', context=ctx)


def schedule(request):
    if(request.GET.get('sendPost')):
        putPost({"id": "2", "message": request.GET.get('message')})
    return render(request, 'schedule.html')
