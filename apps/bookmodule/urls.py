from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),  # Home Page
    path('list_books/', views.list_books, name="books.list_books"),  # List of Books
    path('aboutus/', views.aboutus, name="books.aboutus"),  # About Us
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  # View Book Details

    # Lab 5 - HTML tasks
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.text_formatting, name="books.text_formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),

    # Lab 6 - Search Form
    path('search/', views.search, name="books.search"),  # ✅ تعديل هنا

    # Lab 7 - ORM Queries
    path('books/', views.book_list, name="books.list"),
    path('books/simple/query/', views.simple_query, name='books.simple_query'),
    path('complex/query/', views.complex_query, name='books.complex_query'),

]






