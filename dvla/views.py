from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Driver


# Create your views here.

class AddDriver(CreateView):
    model = Driver
    fields = ('first_name', 'last_name', 'age', 'nationality')
    template_name = 'add_driver.html'
    success_url = '/add_driver/'



