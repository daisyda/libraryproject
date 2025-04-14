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

    # Lab 8
    path('lab8/task1/', views.lab8_task1, name='lab8.task1'),
    path('lab8/task2/', views.lab8_task2, name='books.lab8.task2'),
    path('lab8/task3/', views.lab8_task3, name='books.lab8.task3'),
    path('lab8/task4/', views.lab8_task4, name='books.lab8.task4'),
    path('lab8/task5', views.lab8_task5, name='books.lab8_task5'),
    path('lab8/task7/', views.students_per_city, name='lab8.task7'),

    # Lab 9
    path('lab9/task1/', views.lab9_task1, name='lab9.task1'),
    path('lab9/task2/', views.lab9_task2, name='lab9.task2'),
    path('lab9/task3/', views.lab9_task3, name='lab9.task3'),
    path('lab9/task4/', views.lab9_task4, name='lab9.task4'),
    











]






