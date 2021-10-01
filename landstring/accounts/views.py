from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.user.is_authenticated:
	    return redirect('home')
    else:
        if request.method == 'POST':
            print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Неверный логин или пароль')
        context = {}
        return render(request, 'accounts/login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)
