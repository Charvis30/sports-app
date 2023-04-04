"""sportsApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app1.views import (
    home_view,
    contact,
    about,
)
from sports.views import(
    basketball_data,
    baseball_data,
    hockey_data,
    soccer_data


)
from news.views import(
    news,
)

from trending.views import(
  trending


)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view, name="home"),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('basketball/', basketball_data, name="basketball"),
    path('baseball/', baseball_data, name='baseball'),
    path('hockey/', hockey_data, name='hockey'),
    path('soccer/', soccer_data, name='soccer'),
    path('news/', news, name="news"),
    path('trending/', trending, name='trending')
]
