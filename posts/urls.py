from django.urls import path
from . import views  

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('create/', views.PostCreateView.as_view()),
    path('detail/', views.PostDetailView.as_view()),
    path('delete/', views.PostDeleteView.as_view()),
]