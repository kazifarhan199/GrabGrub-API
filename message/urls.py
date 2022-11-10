from django.urls import path
from . import views  

urlpatterns = [
    path('', views.MessageListView.as_view()),
    path('create/', views.MessageCreateView.as_view()),
]