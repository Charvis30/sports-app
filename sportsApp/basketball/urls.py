from django.urls import path
from . import views

urlpatterns = [
    path('basketball/', views.basketball_data, name='basketball_data'),
]
