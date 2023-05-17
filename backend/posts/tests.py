from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post, Comment, CommentReply, CommentLike, CommentReplyLike, PostLike


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )

        cls.comment = Comment.objects.create(
            author=cls.user,
            post=cls.post,
            body="Nice body content",
        )

        cls.comment2 = Comment.objects.create(
            author=cls.user,
            post=cls.post,
            body="Nice body content # 2",
        )


    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "A good title")
        
    
    def test_comment_model(self):
        self.assertEqual(self.comment2.author.username, "testuser")
        self.assertEqual(self.comment2.post, self.post)
        self.assertEqual(self.comment2.body, "Nice body content # 2")
        self.assertEqual(int(self.comment2), 2)

    # def test_comment_reply_model(self):
    #     self.assertEqual(self.post.author.username, "testuser")
    #     self.assertEqual(self.post.title, "A good title")
    #     self.assertEqual(self.post.body, "Nice body content")
    #     self.assertEqual(str(self.post), "A good title")

    # def test_post_like_model(self):
    #     self.assertEqual(self.post.author.username, "testuser")
    #     self.assertEqual(self.post.title, "A good title")
    #     self.assertEqual(self.post.body, "Nice body content")
    #     self.assertEqual(str(self.post), "A good title")

    # def test_comment_like_model(self):
    #     self.assertEqual(self.post.author.username, "testuser")
    #     self.assertEqual(self.post.title, "A good title")
    #     self.assertEqual(self.post.body, "Nice body content")
    #     self.assertEqual(str(self.post), "A good title")

    # def test_comment_reply_like_model(self):
    #     self.assertEqual(self.post.author.username, "testuser")
    #     self.assertEqual(self.post.title, "A good title")
    #     self.assertEqual(self.post.body, "Nice body content")
    #     self.assertEqual(str(self.post), "A good title")