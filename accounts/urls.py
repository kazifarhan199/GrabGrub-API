from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('profile/<pk>/', views.Profile.as_view(), name='profile'),
    path('profile-edit/', views.ProfileEdit.as_view(), name='profile-edit'),
]