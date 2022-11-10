from rest_framework import serializers
from .models import Posts, trackLikes

class PostsSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()

    def get_user_username(self, obj):
        return obj.user.username
    
    class Meta:
        model = Posts
        fields = ['id', 'text', 'image', 'likes', 'comments', 'user', "user_username"]



class LikesSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        return obj.user.id
    
    post_id = serializers.SerializerMethodField()

    def get_post_id(self, obj):
        return obj.user.id

    class Meta:
        model = trackLikes
        fields = ['user_id', "post_id"]
    