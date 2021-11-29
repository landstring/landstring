from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Comments, Ideas
from .models import PersonalProject, Stage_of_PersonalProject, Task_of_PersonalProject

from .forms import CreateProjectForm, CreateStageForm, CreateTaskForm, CreateUserForm, CommentForm, CreateIdeaForm

# АВТОРИЗАЦИЯ и РЕГИСТРАЦИЯ 
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
		return render(request, 'accounts/main/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
	    return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Неверный логин или пароль')
        context = {}
        return render(request, 'accounts/main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

#ДОМАШНАЯ СТРАНИЦА
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'accounts/main/home.html', context)
#СТАРТАПЫ
@login_required(login_url='login')
def startups(request):
    ideas = Ideas.objects.all().order_by('-id')
    context = {'ideas': ideas}
    return render(request, 'accounts/startups/startups.html', context)

@login_required(login_url='login')
def startupView(request, id):
    idea = Ideas.objects.get(id = id)
    comments = Comments.objects.filter(idea = idea).order_by('-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        text = form.data.get('comment')
        comment = Comments(comment=text, author = request.user, idea = idea)
        comment.save()
    form = CommentForm(None)
    return render(request, 'accounts/startups/idea_detail.html', {'idea' : idea, 'comments' : comments, 'form' : form}) 


@login_required(login_url='login')
def my_startups(request):
    ideas = Ideas.objects.filter(creator=request.user.id).order_by('-id')
    context = {'ideas': ideas}
    return render(request, 'accounts/startups/startups.html', context)

@login_required(login_url='login')
def new_startup(request):
    if request.method == 'POST':
        form = CreateIdeaForm(request.POST)
        name = form.data.get('name')
        description = form.data.get('description')
        idea = Ideas(name=name, description = description, creator=request.user)
        idea.save()
        return redirect('startups')
    else:
        form = CreateIdeaForm(None)
        context = {'form' : form}
        return render(request, 'accounts/startups/new_startup.html', context)
#ПРОЕКТЫ
@login_required(login_url='login')
def projects(request):
    personal_projects = PersonalProject.objects.filter(author = request.user.id).filter(completed = False).order_by('-id')
    finished_personal_projects =  PersonalProject.objects.filter(author = request.user.id).filter(completed = True).order_by('-id')
    context = {'p_p': personal_projects, 'f_p_p':  finished_personal_projects}
    return render(request, 'accounts/projects/projects.html', context)

@login_required(login_url='login')
def projectView(request, id):
    project = PersonalProject.objects.filter(author = request.user.id).filter(id = id)
    if project:
        project = PersonalProject.objects.filter(author = request.user.id).get(id = id)
        stages = Stage_of_PersonalProject.objects.filter(project = id).order_by('-id')
        tasks = []
        for stage in stages:
            tasks.append(Task_of_PersonalProject.objects.filter(stage = stage.id)) 
        return render(request, 'accounts/projects/personal_project_view.html', {'project' : project, 'stages' : stages, 'tasks' : tasks})
    else:
        return render(request, 'accounts/projects/personal_project_view_error.html')

@login_required(login_url='login')
def createStage(request, id):
    project = PersonalProject.objects.filter(author = request.user.id).filter(id = id)
    if project:
        if request.method == 'POST':
            form = CreateStageForm(request.POST)
            name = form.data.get('name')
            description = form.data.get('description')
            stage = Stage_of_PersonalProject(name=name, description = description, project = PersonalProject.objects.filter(author = request.user.id).get(id = id), completed = False)
            stage.save()
            return redirect('./')
        else:
            form = CreateStageForm(None)
            context = {'form' : form}
            return render(request, 'accounts/projects/create_stage.html', context)

@login_required(login_url='login')
def createTask(request, id, id1):
    project = PersonalProject.objects.filter(author = request.user.id).filter(id = id)
    if project:
        if request.method == 'POST':
            form = CreateTaskForm(request.POST)
            name = form.data.get('name')
            task = Task_of_PersonalProject(name=name, stage = Stage_of_PersonalProject.objects.get(id = id1), completed = False)
            task.save()
            return redirect('../')
        else:
            form = CreateTaskForm(None)
            context = {'form' : form}
            return render(request, 'accounts/projects/create_task.html', context)

@login_required(login_url='login')
def completeTask(request, id, id1, id2):
    project = PersonalProject.objects.filter(author = request.user.id).filter(id = id)
    if project:
        task = Task_of_PersonalProject.objects.get(id = id2)
        if task.completed:
            task.completed = False
        else:
            task.completed = True 
        task.save()
        stage = Stage_of_PersonalProject.objects.get(id = id1)
        tasks = Task_of_PersonalProject.objects.filter(stage = stage)
        flag = True
        for i in tasks:
            if not i.completed:
                flag = False
                break
            
        stage.completed = flag
        stage.save()
    
        project = PersonalProject.objects.get(id = id)
        stages = Stage_of_PersonalProject.objects.filter(project = project)
        flag = True 
        for i in stages:
            if not i.completed:
                flag = False
                break
        project.completed = flag
        project.save()
        return redirect('../')

@login_required(login_url='login')
def new_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        name = form.data.get('name')
        description = form.data.get('description')
        project = PersonalProject(name=name, description = description, author=request.user, completed = False)
        project.save()
        return redirect('projects')
    else:
        form = CreateIdeaForm(None)
        context = {'form' : form}
        return render(request, 'accounts/projects/new_project.html', context)

#КОМАНДЫ
@login_required(login_url='login')
def team_projects(request):
    context = {}
    return render(request, 'accounts/projects/team_projects.html', context)

@login_required(login_url='login')
def teams(request):
    context = {}
    return render(request, 'accounts/teams/teams.html', context)

@login_required(login_url='login')
def my_team(request):
    context = {}
    return render(request, 'accounts/teams/my_teams.html', context)

@login_required(login_url='login')
def new_team(request):
    context = {}
    return render(request, 'accounts/teams/new_team.html', context)

@login_required(login_url='login')
def articles(request):
    context = {}
    return render(request, 'accounts/articles/articles.html', context)

@login_required(login_url='login')
def my_articles(request):
    context = {}
    return render(request, 'accounts/articles/my_articles.html', context)

@login_required(login_url='login')
def new_articles(request):
    context = {}
    return render(request, 'accounts/articles/new_article.html', context)

@login_required(login_url='login')
def learning(request):
    context = {}
    return render(request, 'accounts/learning.html', context)

@login_required(login_url='login')
def account(request):
    context = {}
    return render(request, 'accounts/main/account.html', context)

