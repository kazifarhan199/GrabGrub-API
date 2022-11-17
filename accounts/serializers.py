from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False, validators=[UniqueValidator(User.objects.all())])
    username = serializers.CharField(required=False, validators=[UniqueValidator(User.objects.all())])
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token')
        
    def update(self, instance, validated_data):

        if validated_data.get('password'):
            instance.set_password(validated_data.pop('password'))
            instance.save()
        return super().update(instance, validated_data)

