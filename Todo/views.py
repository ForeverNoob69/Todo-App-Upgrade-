from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from Todo.models import task
from django.urls import reverse_lazy

# Create your views here.


class RegisterPage(FormView):
    template_name = "Todo/register.html"
    form_class = UserCreationForm
    #redirect_authenticated_user = True
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("Home")
        return super(RegisterPage, self).get(*args, **kwargs)


class Custom_Login(LoginView):
    template_name = "Todo/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("Home")


class TaskList(LoginRequiredMixin, ListView):
    model = task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()
        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(
                task__icontains=search_input)
        #context["search_input"] = search_input

        return context


class TaskDetail(LoginRequiredMixin,    DetailView):
    model = task
    context_object_name = "detail"


class TaskCreate(CreateView):
    model = task
    fields = ["task", "description", "complete"]
    template_name = "Todo/create_task.html"
    success_url = reverse_lazy("Home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = task
    fields = ["task", "description", "complete"]
    success_url = reverse_lazy("Home")


class TaskDelete(DeleteView):
    model = task
    success_url = reverse_lazy("Home")
