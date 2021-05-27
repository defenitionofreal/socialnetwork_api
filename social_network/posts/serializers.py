from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    created = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField()
    likes = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'author', 'title', 'slug', 'body', 'created', 'likes')
        #read_only_fields = ['likes', 'created', 'slug']
        model = Post

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


    def get_likes(self, obj):
        return Like.objects.filter(post_id=obj.id).count()


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['post', 'liker', 'liked_at']



