from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('plus', views.plus_2),
    path('user_i', views.user_add),
]
