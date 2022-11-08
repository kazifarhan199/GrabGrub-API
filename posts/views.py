
from .serializers import PostsSerializer
from rest_framework import generics

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostsSerializer
