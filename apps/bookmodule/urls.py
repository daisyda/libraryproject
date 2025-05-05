from django.urls import path
from . import views

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


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

# Lab 10
    path('lab9_part1/listbooks/', views.lab9_part1_listbooks, name='lab9_part1.listbooks'),
    path('lab9_part1/addbook/', views.lab9_part1_addbook, name='lab9_part1.addbook'),
    path('lab9_part1/editbook/<int:id>/', views.lab9_part1_editbook, name='lab9_part1.editbook'),
    path('lab9_part1/deletebook/<int:id>/', views.lab9_part1_deletebook, name='lab9_part1.deletebook'),



# Lab10 Part2 - CRUD باستخدام Django Forms
path('lab9_part2/listbooks/', views.lab9_part2_listbooks, name='lab9_part2.listbooks'),
path('lab9_part2/addbook/', views.lab9_part2_addbook, name='lab9_part2.addbook'),
path('lab9_part2/editbook/<int:id>/', views.lab9_part2_editbook, name='lab9_part2.editbook'),
path('lab9_part2/deletebook/<int:id>/', views.lab9_part2_deletebook, name='lab9_part2.deletebook'),


#lab 11

path('students/', views.student_list, name='student_list'),
path('students/add/', views.student_add, name='student_add'),
path('students/update/<int:pk>/', views.student_update, name='student_update'),
path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

path('students2/', views.student2_list, name='student2_list'),
path('students2/add/', views.student2_add, name='student2_add'),


 path('gallery/upload/', views.gallery_upload, name='gallery_upload'),
]

# ✅ Append static URLs for media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









    



    


















