from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.index),
    path('authors', views.authors),
    path('books/create', views.add_book),
    path('books/<int:book_id>', views.book_info),
    path('books/<int:book_id>/assign', views.assign_book),
    path('authors/create', views.add_author),
    path('authors/<int:author_id>', views.author_info),
    path('authors/<int:author_id>/assign', views.assign_author)
]