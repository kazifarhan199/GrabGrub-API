from django.urls import path
from . import views  

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('create/', views.PostCreateView.as_view()),
]