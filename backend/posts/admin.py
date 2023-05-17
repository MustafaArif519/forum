from django.contrib import admin

from .models import Post, Comment, CommentReply, PostLike, CommentLike, CommentReplyLike


# Register your models here.
admin.site.register(Post)
admin.site.register(CommentReply)
admin.site.register(Comment)