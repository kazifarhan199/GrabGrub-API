from rest_framework import serializers
from .models import Posts, trackLikes, Claim

class PostsSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()

    def get_has_liked(self, obj):
        if trackLikes.objects.filter(user=self.context['request'].user, post=obj).exists():
            return True
        else:
            return False

    def get_user_username(self, obj):
        return obj.user.username
    
    def get_user_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.user.image)

    class Meta:
        model = Posts
        fields = ['id', 'text', 'image', 'likes', 'comments', 'user', "user_username", "user_image", 'date', 'title', 'has_liked', 'servings']



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
    
class ClaimSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        return obj.post.text
        
    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.post.image.url)
        
    class Meta:
        model = Claim
        fields = ["id", "post", "image", "quantity", "user", "text"]

    def validate(self, attrs):
        if self.context['request'].user!=attrs['user']:
             raise serializers.ValidationError("Please login")
        if attrs['post'].servings < attrs['quantity']:
             raise serializers.ValidationError("Not enough quantity to claim")
        return super().validate(attrs)