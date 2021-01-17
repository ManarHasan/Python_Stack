from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('add_user', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('quotes', views.quotes),
    path('add_quote', views.add_quote),
    path('like_quote/<int:quote_id>/<int:user_id>', views.like_quote),
    path('delete_quote/<int:quote_id>', views.delete_quote),
    path('myaccount/<int:user_id>', views.my_account),
    path('user/<int:user_id>', views.user_account),
    path('dislike_quote/<int:quote_id>/<int:user_id>', views.dislike_quote),
    path('edit/<int:user_id>', views.edit_account)

]
