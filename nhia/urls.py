from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddIndividual.as_view(), name='add_nhia'),

]