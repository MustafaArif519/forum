from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post, Comment, CommentLike, PostLike, CommentReplyLike, CommentReply


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
            "created_at",
        )
        model = Comment

# Comment Reply Serial
class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "body",
            "comment",
            "created_at",
        )
        model = CommentReply

# Post Like serial
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "post",
            "created_at",
        )
        model = PostLike

# Comment Like serial
class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "comment",
            "created_at",
        )
        model = CommentLike

# Comment reply like serial
class CommentReplyLikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "comment_reply",
            "created_at",
        )
        model = CommentReplyLike

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)