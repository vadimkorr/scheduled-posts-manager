from services.db.posts import putPost
from django.shortcuts import render
from services.db.posts import getPost
from services.db.posts import getPosts

# Create your views here.


def posts(request):
    posts = getPosts()
    ctx = {"posts": posts}
    return render(request, 'posts.html', context=ctx)


def post(request, id):
    post = getPost(id)
    ctx = {"post": post}
    return render(request, 'post.html', context=ctx)


def newPost(request):
    if(request.GET.get('sendPost')):
        putPost({"id": "2", "message": request.GET.get('message')})
    return render(request, 'new-post.html')
