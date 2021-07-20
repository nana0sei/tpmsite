from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Employee
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

class AddEmployee(CreateView):
    model = Employee
    fields = ('first_name', 'last_name', 'age', 'nationality')
    template_name = 'add_employee.html'
    success_url = '/add_employee/'


def homepage(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h1>Method Not Allowed<h1>")
    else:
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            return HttpResponseRedirect('/home')
        else:
            messages.error(request, "Wrong password. Please retry.")
            return HttpResponseRedirect("/")
