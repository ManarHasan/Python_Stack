from django.urls import path
from . import views

urlpatterns = [
    path('', views.result),
    path('game', views.user_input),
    path('playagain', views.destroy),
    path('leaderboard', views.leaderboard)
]
