from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book-home'),  # Default route for books
]
