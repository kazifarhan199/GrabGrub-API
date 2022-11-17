from django.urls import path
from . import views  

urlpatterns = [
    path('list/<to>/', views.MessageListView.as_view()),
    path('create/', views.MessageCreateView.as_view()),
]