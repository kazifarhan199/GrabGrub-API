from .serializers import MessageSerializer
from .models import Message
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all().order_by('-id')
        
        u = self.request.query_params.get('u', None)
        if u is not None:
            queryset =queryset.filter(user__username__icontains=u)
            
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset =queryset.filter(text__icontains=q)
        
        return queryset
