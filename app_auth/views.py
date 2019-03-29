from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login


def sign_in(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        login(request, user, 'appAuth.auth_backend.AuthBackend')

        print(user)

        # form = {
        #     'username' : username,
        #     'password': passwo
        # }

        # form = AuthenticationForm(data=request.POST)
        # if form.is_valid():
        render(request, 'posts.html')
        # redirect('/posts/')
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in.html', {'form': form})


def sign_up(request):
    return render(request, 'sign-up.html')
