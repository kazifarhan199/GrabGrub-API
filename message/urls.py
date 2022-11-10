from django.urls import path
from . import views  

urlpatterns = [
    path('create/', views.MessageCreateView.as_view()),
    # path('create/', views.PostCreateView.as_view()),
]