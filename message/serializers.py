from rest_framework import serializers 
from .models import Message, Conversation

class MessageSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    to_username = serializers.SerializerMethodField()
    to_email = serializers.SerializerMethodField()
    post_image = serializers.SerializerMethodField()
    post_text = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()
    to_image = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.id

    def get_post_image(self, obj):
        if obj.post:
            return self.context['request'].build_absolute_uri(obj.post.image.url)
        else:
            return ''

    def get_post_text(self, obj):
        if obj.post:
            return obj.post.text
        else:
            return ''

    def get_user_username(self, obj):
        return obj.user.username

    def get_to_username(self, obj):
        return obj.to.username

    def get_to_email(self, obj):
        return obj.to.email

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


    def get_to_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.to.image)

    def get_user_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.user.image)



class ConversationSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    to_username = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()
    to_image = serializers.SerializerMethodField()
    to_email = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = "__all__"

    def get_to_email(self, obj):
        return obj.to.email

    def get_user(self, obj):
        return obj.user.id

    def get_user_username(self, obj):
        return obj.user.username

    def get_to_username(self, obj):
        return obj.to.username

    def get_to_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.to.image)

    def get_user_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.user.image)