from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),  # Home Page
    path('list_books/', views.list_books, name="books.list_books"),  # List of Books
    path('aboutus/', views.aboutus, name="books.aboutus"),  # About Us
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  # View Book Details
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.text_formatting, name="books.text_formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('search/', views.search_books, name="books.search"),





]
