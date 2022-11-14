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

    class Meta:
        model = trackLikes
        fields = ['user', "post"]

    def validate(self, data):
        if trackLikes.objects.filter(user=self.context['request'].user, post=data['post']).exists():
            raise serializers.ValidationError("You have already a placed like on this post")
        return data
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    