from rest_framework import serializers 
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    to_username = serializers.SerializerMethodField()
    post_image = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.id

    def get_post_image(self, obj):
        if obj.post:
            return self.context['request'].build_absolute_uri(obj.post.image.url)
        else:
            return ''

    def get_user_username(self, obj):
        return obj.user.username

    def get_to_username(self, obj):
        return obj.to.username

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Message
        fields = "__all__"

    def validate(self, data):
        data = super().validate(data)
        if not data.get('text', None) and not data.get('image', None) and not data.get('post', None):
            raise serializers.ValidationError("Please specify what to send")
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)