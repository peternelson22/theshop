from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.success(request, 'account successfully created')
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')
