from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .forms import CreateUserForm



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
			    form.save()
			    user = form.cleaned_data.get('username')
			    messages.success(request, 'Account was created for ' + user)

			    return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

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

@login_required(login_url='login')
def startups(request):
    context = {}
    return render(request, 'accounts/startups.html', context)

@login_required(login_url='login')
def my_startups(request):
    context = {}
    return render(request, 'accounts/my_startups.html', context)

@login_required(login_url='login')
def new_startup(request):
    context = {}
    return render(request, 'accounts/new_startup.html', context)

@login_required(login_url='login')
def projects(request):
    context = {}
    return render(request, 'accounts/projects.html', context)

@login_required(login_url='login')
def new_project(request):
    context = {}
    return render(request, 'accounts/new_project.html', context)

@login_required(login_url='login')
def teams(request):
    context = {}
    return render(request, 'accounts/teams.html', context)

@login_required(login_url='login')
def my_teams(request):
    context = {}
    return render(request, 'accounts/my_teams.html', context)

@login_required(login_url='login')
def new_team(request):
    context = {}
    return render(request, 'accounts/new_team.html', context)

@login_required(login_url='login')
def articles(request):
    context = {}
    return render(request, 'accounts/articles.html', context)

@login_required(login_url='login')
def my_articles(request):
    context = {}
    return render(request, 'accounts/my_articles.html', context)

@login_required(login_url='login')
def new_articles(request):
    context = {}
    return render(request, 'accounts/new_articles.html', context)

@login_required(login_url='login')
def learning(request):
    context = {}
    return render(request, 'accounts/learning.html', context)

@login_required(login_url='login')
def account(request):
    context = {}
    return render(request, 'accounts/account.html', context)