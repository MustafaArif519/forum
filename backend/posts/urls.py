from django.urls import path

from .views import UserViewSet, PostViewSet, CommentViewSet, CommentReplyViewSet,\
                   PostLikeViewSet, CommentLikeViewSet, CommentReplyLikeViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")
router.register("comment-replys", CommentReplyViewSet, basename="comment_replys")
router.register("post-likes", PostLikeViewSet, basename="post_likes")
router.register("comment-likes", CommentLikeViewSet, basename="comment_likes")
router.register("comment-reply-likes", CommentReplyLikeViewSet, basename="comment_reply_likes")

urlpatterns = router.urls
