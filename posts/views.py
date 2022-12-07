
from .serializers import LikesSerializer, PostsSerializer, ClaimSerializer
from .models import Posts, trackLikes, Claim
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostsSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        queryset = Posts.objects.all().order_by('-id')
        
        l = self.request.query_params.get('l', None)
        if l is not None:
            u = self.request.query_params.get('u', None)
            if u is not None:
                user = get_object_or_404(User.objects.all(), username=u)
                t = [t.post for t in trackLikes.objects.filter(user=user)]
                queryset = t
        
        else:
            u = self.request.query_params.get('u', None)
            if u is not None:
                queryset =queryset.filter(user__username__iexact=u)
        
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset =queryset.filter(title__icontains=q)

        
        return queryset

class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostsSerializer
    queryset= Posts.objects.all()

class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostsSerializer
    queryset= Posts.objects.all()

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikesSerializer

class LikeDeleteView(generics.DestroyAPIView):
    
    def get_queryset(self):
        return trackLikes.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, post=self.kwargs['post'])

class ClaimCreateView(generics.CreateAPIView):
    serializer_class = ClaimSerializer

class ClaimListView(generics.ListAPIView):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return Claim.objects.filter(user=self.request.user).order_by("-id")
