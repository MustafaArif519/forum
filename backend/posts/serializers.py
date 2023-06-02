from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "body",
            "post",
            "parent_comment",
            "created_at",
        )
        model = Comment


# Like serialization
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "post",
            "comment",
            "created_at",
        )
        model = Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)