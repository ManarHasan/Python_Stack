from django.urls import path
from . import views

urlpatterns = [
    path('', views.dojo),
    path('addinfo', views.submit),
    # path('result', views.result)
]
