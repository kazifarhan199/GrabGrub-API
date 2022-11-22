from django.urls import path
from . import views  

urlpatterns = [
    path('conversations/', views.ConversationListView.as_view()),
    path('list/<to>/', views.MessageListView.as_view()),
    path('create/', views.MessageCreateView.as_view()),
]