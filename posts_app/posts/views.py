from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse

from . import models
from .models import Posts, Complaints


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is None:
            return render(request, 'login.html', {})
        else:
            login(request, user)
            return redirect(reverse('home'))
    else:
        raise Exception('Method is not allowed')


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse('login'))


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'register.html', {})
    elif request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create(
            username=email,
            password=make_password(password),
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect(reverse('login'))
    else:
        raise Exception('Method is not allowed')


def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        title = str(request.POST.get('title')).strip()
        if len(title) < 1:
            raise Exception('Too short title')

        description = str(request.POST.get('description')).strip()
        Posts.objects.create(
            author=request.user.username,
            title=title,
            description=description
        )
        return redirect(reverse('home'))
    else:
        raise Exception('Method is not allowed')


def home(request: HttpRequest) -> HttpResponse:
    posts_obj = Posts.objects.all().filter(is_moderate='True')
    return render(request, 'list.html', {'list': posts_obj})


def create_complaints(request: HttpRequest, pk: str) -> HttpResponse:
    post = models.Posts.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'complaints.html', {'pk': pk})
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Complaints.objects.create(
            post=post,
            title=title,
            description=description
        )

        return redirect(reverse('home'))
    else:
        raise Exception('Method is not allowed!')

