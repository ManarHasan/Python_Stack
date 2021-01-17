from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money),
    path('process_money/<str:name>', views.process_money),
    path('delete', views.delete),
    path('add_rules', views.add_rules),
    path('win', views.win),
    path('lose', views.lose)
]
