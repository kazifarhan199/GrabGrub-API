
from .serializers import LikesSerializer, PostsSerializer
from .models import Posts
from rest_framework import generics

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostsSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        queryset = Posts.objects.all().order_by('-id')
        
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset =queryset.filter(title__icontains=q)

        q = self.request.query_params.get('u', None)
        if q is not None:
            queryset =queryset.filter(user__username__iexact=q)
        
        return queryset

class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostsSerializer
    queryset= Posts.objects.all()

class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostsSerializer
    queryset= Posts.objects.all()

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikesSerializer