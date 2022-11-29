from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers

User = get_user_model()


class Register(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserRegisterSerializer

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        data = serializers.UserSerializer(user, context={'request': request}).data
        data['token'] = user.token
        return Response(data)

class Profile(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

class ProfileEdit(UpdateAPIView):
    serializer_class = serializers.UserSerializer
    
    def get_object(self):
        return User.objects.get(pk=self.request.user.id)
