from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ContactMessage, ServiceRegistration

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid username or password'})
    return render(request, 'main/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname
        )
        ServiceRegistration.objects.create(
            full_name=f"{firstname} {lastname}",
            email=email,
            service='General Registration'
        )
        messages.success(request, f'Account created! You can now login, {firstname}!')
        return redirect('login')
    return render(request, 'main/register.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'main/about.html')

@login_required(login_url='login')
def services(request):
    return render(request, 'main/services.html')

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=msg)
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    return render(request, 'main/contact.html')
