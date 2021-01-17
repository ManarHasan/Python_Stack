from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('register', views.register),
    path('login', views.login),
    path('welcome/<int:id>', views.welcome),
    path('logout', views.logout),
    path('add/<int:user_id>/<int:wish_id>', views.add),
    path('remove/<int:user_id>/<int:wish_id>', views.remove),
    path('new_wish', views.new_wish_page),
    path('new_wish/<int:user_id>', views.new_wish)
]
