from django.urls import path, include
from . import views


app_name = 'auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/<int>/', views.profile)
]
