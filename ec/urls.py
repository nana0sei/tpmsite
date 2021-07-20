from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddEmployee.as_view(), name='add_employee'),

]