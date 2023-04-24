from django.urls import path
from . import views

urlpatterns = [
    path('nbateams/', views.nba_teams, name='nbateams'),
    
]