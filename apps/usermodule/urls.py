from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user-home'),  # Default route for users
]
