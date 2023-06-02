from django.urls import path

from .views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")
router.register("likes", LikeViewSet, basename="likes")

urlpatterns = router.urls
