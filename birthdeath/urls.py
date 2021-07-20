from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddPerson.as_view(), name='add_person'),

]