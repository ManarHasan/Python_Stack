from django.urls import path
from . import views
urlpatterns = [
    path('', views.root_method),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method),
    path("render", views.index)
]
