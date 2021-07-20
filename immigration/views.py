from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .models import Individual


# Create your views here.

class AddIndividual(CreateView):
    model = Individual
    fields = ('first_name', 'last_name', 'age', 'gender', 'nationality')
    template_name = 'add_individual.html'
    success_url = '/add_individual/'
