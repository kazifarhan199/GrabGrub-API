from rest_framework import serializers 
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    to_username = serializers.SerializerMethodField()

    def get_user_username(self, obj):
        return obj.user.username
    
    def get_to_username(self, obj):
        return obj.to.username

    class Meta:
        model = Message
        fields = "__all__"