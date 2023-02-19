from django.urls import path
from scoreboard.views import *

urlpatterns = [
    path('newrecord/', NewRecord),
    path('leaderboard/', ScoreBoardView)
]
