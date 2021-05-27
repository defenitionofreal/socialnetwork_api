from django.test import TestCase
from users.models import User
from .models import Post, Like


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # create a post
        test_post = Post.objects.create(
            author=testuser1,
            title='Post title',
            slug='post-title',
            body='Post content...'
        )
        test_post.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_slug = f'{post.slug}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Post title')
        self.assertEqual(expected_slug, 'post-title')
        self.assertEqual(expected_body, 'Post content...')

    def test_likes(self):
        like = Like.object.get()
