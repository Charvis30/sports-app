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

from rosters.views import(
    nba_teams,
    la_roster,
    ny_roster,
    lac_roster,
    okc_roster,
    san_roster,
    utah_roster,
    miami_roster,
    boston_roster,
    dallas_roster,
    denver_roster,
    philly_roster,
    atlanta_roster,
    chicago_roster,
    detroit_roster,
    houston_roster,
    indiana_roster,
    memphis_roster,
    orlando_roster,
    phoenix_roster,
    toronto_roster,
    brooklyn_roster,
    portland_roster,
    charlotte_roster,
    cleveland_roster,
    milwaukee_roster,
    minnesota_roster,
    neworleans_roster,
    sacramento_roster,
    washington_roster,
    goldenstate_roster,
   
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

    #news
    path('news/', news, name="news"),
    path('trending/', trending, name='trending'),

    #rosters (nba)
    path('nbateams/', nba_teams, name='nbateams'),
    path('lakers/', la_roster, name='Lakers'),
    path('clippers/', lac_roster, name='Clippers'),
    path('warriors/', goldenstate_roster, name='Warriors'),
    path('knicks/', ny_roster, name='Knicks'),
    path('thunder/', okc_roster, name='Thunder'),
    path('spurs/', san_roster, name='Spurs'),
    path('jazz/', utah_roster, name='Jazz'),
    path('heat/', miami_roster, name='Heat'),
    path('celtics/', boston_roster, name='Celtics'),
    path('mavericks/', dallas_roster, name='Mavericks'),
    path('nuggets/', denver_roster, name='Nuggets'),
    path('sixers/', philly_roster, name='76ers'),
    path('hawks/', atlanta_roster, name='Hawks'),
    path('bulls/', chicago_roster, name='Bulls'),
    path('pistons/', detroit_roster, name='Pistons'),
    path('rockets/', houston_roster, name='Rockets'),
    path('pacers/', indiana_roster, name='Pacers'),
    path('grizzlies/', memphis_roster, name='Grizzlies'),
    path('magic/', orlando_roster, name='Magic'),
    path('suns/', phoenix_roster, name='Suns'),
    path('raptors/', toronto_roster, name='Raptors'),
    path('nets/', brooklyn_roster, name='Nets'),
    path('blazers/', portland_roster, name='Trail Blazers'),
    path('hornets/', charlotte_roster, name='Hornets'),
    path('cavaliers/', cleveland_roster, name='Cavaliers'),
    path('bucks/', milwaukee_roster, name='Bucks'),
    path('timberwolves/', minnesota_roster, name='Timberwolves'),
    path('pelicans/', neworleans_roster, name='Pelicans'),
    path('kings/', sacramento_roster, name='Kings'),
    path('wizards/', washington_roster, name='Wizards'),
]
