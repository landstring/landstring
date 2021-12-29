from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('', views.home, name="home"),

    path('startups/', views.startups, name="startups"),
    path('my_startups/', views.my_startups, name="my_startups"),
    path('my_startups/<int:id>/', views.startupView),
    path('new_startup/', views.new_startup, name="new_startup"),
    path('startups/<int:id>/', views.startupView),

    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>/', views.projectView),
    path('projects/<int:id>/create-stage', views.createStage),
    path('projects/<int:id>/<int:id1>/create-task', views.createTask),
    path('projects/<int:id>/<int:id1>/<int:id2>', views.completeTask),
    path('team-projects/', views.team_projects, name="team_projects"),
    path('new-project/', views.new_project, name="new_project"),

    path('my_team/', views.my_team, name="my_team"),
    path('new_team/', views.new_team, name="new_team"),
    path('my_team/create-application', views.create_application),

    path('learning/', views.learning, name="learning"),


    path('account/', views.account, name="account"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
