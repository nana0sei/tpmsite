from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Person


# Create your views here.

class AddPerson(CreateView):
    model = Person
    fields = ('first_name', 'last_name', 'age', 'gender', 'nationality')
    template_name = 'add_person.html'
    success_url = '/add_person/'



