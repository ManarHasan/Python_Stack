from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add_book', views.add_books),
    path('book/<int:id>', views.book_profile),
    path('add_author_to_book/book<int:id>/add_author', views.add_author_to_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('author/<int:id>', views.author_profile),
    path('add_book_to_author/author<int:id>/add_book', views.add_book_to_author)
]
