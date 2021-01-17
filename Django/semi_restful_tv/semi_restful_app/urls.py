from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows/new', views.new_show),
    path('add_show', views.add_show),
    path('shows', views.all_shows),
    path('edit/<int:i>', views.edit_page),
    path('edit_show/<int:i>', views.edit),
    path('show_profile/<int:i>', views.profile),
    path('delete/<int:i>', views.delete)

]
