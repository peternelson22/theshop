from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def loginnow(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, 'users/login.html')

def logoutnow(request):
    logout(request)
    return redirect('login')

def registernow(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist, try another.')
            elif User.objects.filter(username=username).exists():
                messages.error(request,'username already taken')
            else:
                user = User.objects.create_user(username=username,  password=password, email=email)
                user.save()
                messages.success(request, 'account successfully created')
                userlogin = auth.authenticate(username=username, password=password)
                auth.login(request, userlogin)
                return redirect('home')
        else: 
            messages.error(request, 'passwords do not match')
            return redirect('register')    
    return render(request, 'users/register.html')


