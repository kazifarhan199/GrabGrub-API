from .serializers import MessageSerializer
from .models import Message
from rest_framework import generics

class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer