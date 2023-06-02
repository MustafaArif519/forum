from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

from .models import Post, Comment, Like
from .serializers import PostSerializer, UserSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer