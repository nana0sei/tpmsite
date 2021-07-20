from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Individual


# Create your views here.

class AddIndividual(CreateView):
    model = Individual
    fields = ('first_name', 'last_name', 'age', 'gender', 'nationality')
    template_name = 'add_nhia.html'
    success_url = '/add_nhia/'



