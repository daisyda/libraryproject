from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView




urlpatterns = [
    path('register/', views.register_view, name='register'),

    
    # ✅ Login page using built-in view
    path('login/', auth_views.LoginView.as_view(template_name='usermodule/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),



path('login/', CustomLoginView.as_view(), name='login'),

]
