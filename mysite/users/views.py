from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from mysite import settings
from django.core.cache import cache
import pickle


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='bible:root_from_users')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='users:login')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='bible:root_from_users')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')
        login(request, user)
        cache.set('userid', request.user.id)
        return redirect(to='bible:root_from_users')

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    cache.delete('userid')
    return redirect(to='bible:root_from_users')
