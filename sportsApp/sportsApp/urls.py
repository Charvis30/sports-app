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
from django.urls import include, path
from app1.views import (
    home_view,
    contact,
    about,
)
from sports.views import(
    basketball_data,
    baseball_data,
    hockey_data,
    soccer_data,
    football_data


)
from news.views import(
    news,
)

from trending.views import(
  trending

)

from rosters.views import(
    nba_teams, nba_roster,
    mlb_teams,
    nfl_teams,
    nhl_teams,





    orioles_roster, red_sox_roster, white_sox_roster, 
    tigers_roster, astros_roster, royals_roster, angels_roster, twins_roster, 
    yankees_roster, athletics_roster, mariners_roster, rays_roster, rangers_roster,
    blue_jays_roster, dbacks_roster, braves_roster, cubs_roster, reds_roster, rockies_roster, 
    dodgers_roster, marlins_roster, brewers_roster, mets_roster, phillies_roster, pirates_roster, padres_roster, 
    giants_roster, cardinals_roster, nationals_roster, guardians_roster,

    
   
)

urlpatterns = [
    path("admin/", admin.site.urls),

    #app1
    path('', home_view, name="home"),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

    #sports
    path('basketball/', basketball_data, name="basketball"),
    path('baseball/', baseball_data, name='baseball'),
    path('hockey/', hockey_data, name='hockey'),
    path('soccer/', soccer_data, name='soccer'),
    path('football/', football_data, name='football'),

    #news
    path('news/', news, name="news"),
    path('trending/', trending, name='trending'),

    #rosters (nba)
    path('nbateams/', nba_teams, name='nbateams'),

   

    ##MLB##
    path('mlbteams/', mlb_teams, name='mlbteams'),

    path('yankees/', yankees_roster, name='Yankees'),
    path('redsox/', red_sox_roster, name='Red Sox'),
    path('orioles/', orioles_roster, name='Orioles'),
    path('rays/', rays_roster, name='Rays'),
    path('bluejays/', blue_jays_roster, name='Blue Jays'),
    path('whitesox/', white_sox_roster, name='White Sox'),
    path('tigers/', tigers_roster, name='Tigers'),
    path('royals/', royals_roster, name='Royals'),
    path('twins/', twins_roster, name='Twins'),
    path('astros/', astros_roster, name='Astros'),
    path('angels/', angels_roster, name='Angels'),
    path('athletics/', athletics_roster, name='Athletics'),
    path('mariners/', mariners_roster, name='Mariners'),
    path('rangers/', rangers_roster, name='Rangers'),
    path('braves/', braves_roster, name='Braves'),
    path('marlins/', marlins_roster, name='Marlins'),
    path('mets/', mets_roster, name='Mets'),
    path('phillies/', phillies_roster, name='Phillies'),
    path('nationals/', nationals_roster, name='Nationals'),
    path('cubs/', cubs_roster, name='Cubs'),
    path('reds/', reds_roster, name='Reds'),
    path('brewers/', brewers_roster, name='Brewers'),
    path('pirates/', pirates_roster, name='Pirates'),
    path('cardinals/', cardinals_roster, name='Cardinals'),
    path('diamondbacks/', dbacks_roster, name='Diamondbacks'),
    path('rockies/', rockies_roster, name='Rockies'),
    path('dodgers/', dodgers_roster, name='Dodgers'),
    path('padres/', padres_roster, name='Padres'),
    path('giants/', giants_roster, name='Giants'),
    path('guardians/', guardians_roster, name='Guardians'),


    ##NFL
    path('nflteams/', nfl_teams, name='nflteams'),
    
    path("rosters/", include("rosters.urls")),

    ##NHL
    path('nhlteams/', nhl_teams, name='nhlteams'),


    

]
