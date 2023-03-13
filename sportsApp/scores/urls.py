from django.urls import path
from . import views

urlpatterns = [
    path('score/<str:team>/', views.live_score, name='live_score'),
]
