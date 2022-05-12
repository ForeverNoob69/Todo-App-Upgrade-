from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register", views.RegisterPage.as_view(), name="register"),
    path("login", views.Custom_Login.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("", views.TaskList.as_view(), name="Home"),
    path("task/<str:pk>/", views.TaskDetail.as_view(), name="task_details"),
    path("create_task", views.TaskCreate.as_view(), name="create_task"),
    path("task-update/<str:pk>", views.TaskUpdate.as_view(), name="task_update"),
    path("task-delete/<str:pk>", views.TaskDelete.as_view(), name="task_delete"),
]
