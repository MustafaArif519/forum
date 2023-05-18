from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

from .models import Post, Comment, CommentLike, PostLike, CommentReply, CommentReplyLike
from .serializers import PostSerializer, UserSerializer, CommentSerializer, CommentReplySerializer,\
                         PostLikeSerializer, CommentLikeSerializer, CommentReplyLikeSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentReplyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer

class PostLikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

class CommentLikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

class CommentReplyLikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CommentReplyLike.objects.all()
    serializer_class = CommentReplyLikeSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer