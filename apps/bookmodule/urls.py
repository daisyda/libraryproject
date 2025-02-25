from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),  # Home Page
    path('list_books/', views.list_books, name="books.list_books"),  # List of Books
    path('aboutus/', views.aboutus, name="books.aboutus"),  # About Us
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  # View Book Details
]
