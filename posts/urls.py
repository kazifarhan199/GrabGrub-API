from django.urls import path
from . import views  

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('create/', views.PostCreateView.as_view()),
    path('detail/<pk>/', views.PostDetailView.as_view()),
    path('delete/<pk>/', views.PostDeleteView.as_view()),
    path('like/add/', views.LikeCreateView.as_view()),
    path('like/remove/<post>/', views.LikeDeleteView.as_view()),
    path('claim/add/', views.ClaimCreateView.as_view()),
    path('claim/', views.ClaimListView.as_view()),
]