from django.urls import path
from . import views

urlpatterns = [
    path('basketball/', views.basketball_data, name='basketball_data'),
    path('baseball/', views.baseball_data, name='baseball_data'),
    path('hockey/', views.hockey_data, name='hockey_data'),
    path('soccer/', views.soccer_data, name='soccer_data'),
    path('football/', views.football_data, name='football_data'),
]
