from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('add', views.add),
    path('delete/<int:i>', views.delete)
]
