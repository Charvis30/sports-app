from django.urls import path
from . import views

urlpatterns = [
    path('basketball/', views.basketball_data, name='basketball_data'),
    path('games/', views.get_games_data, name='games'),
]
