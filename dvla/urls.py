from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddDriver.as_view(), name='add_driver'),

]