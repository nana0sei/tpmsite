"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import ec.views
import dvla.views
import nhia.views
import birthdeath.views
from ec import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_employee/', include('ec.urls'), name='add_employee'),
    path('add_nhia/', include('nhia.urls'), name='add_nhia'),
    path('add_driver/', include('dvla.urls'), name='add_driver'),
    path('add_person/', include('birthdeath.urls'), name='add_person'),
    path('home/', views.homepage, name="homepage"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('', views.login, name="login"),

]
