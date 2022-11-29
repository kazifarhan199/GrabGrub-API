from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False, validators=[UniqueValidator(User.objects.all())])
    username = serializers.CharField(required=False, validators=[UniqueValidator(User.objects.all())])
    bio = serializers.CharField(required=False)
    image_url = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(required=False, write_only=True)
    password = serializers.CharField(required=False, write_only=True)

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.profile.image.url)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'image', 'bio', 'image_url', 'password')
        
    def update(self, instance, validated_data):
        if validated_data.get('bio'):
            instance.profile.bio = validated_data.pop('bio')
            instance.profile.save()
        if validated_data.get('image'):
            instance.profile.image = validated_data.pop('image')
            instance.profile.save()
        if validated_data.get('password'):
            instance.set_password(validated_data.pop('password'))
            instance.save()
        return super().update(instance, validated_data)


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False, validators=[UniqueValidator(User.objects.all())])
    username = serializers.CharField(required=False, validators=[UniqueValidator(User.objects.all())])
    bio = serializers.CharField(required=False)
    image_url = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(required=False, write_only=True)
    password = serializers.CharField(required=False, write_only=True)

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.profile.image.url)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'image', 'bio', 'image_url', 'password', 'token')
        
    def update(self, instance, validated_data):
        if validated_data.get('bio'):
            instance.profile.bio = validated_data.pop('bio')
            instance.profile.save()
        if validated_data.get('image'):
            instance.profile.image = validated_data.pop('image')
            instance.profile.save()
        if validated_data.get('password'):
            instance.set_password(validated_data.pop('password'))
            instance.save()
        return super().update(instance, validated_data)