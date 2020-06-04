from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.conf import settings
import os
# Create your tests here.

class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create(username='Todun', password='todun12345')
        testuser.save()
        testpost = Post.objects.create(title='Test title', subtitle='simple post', image=os.path.join(settings.BASE_DIR, 'media/posts_pics/header-img.png'), author=testuser, content='Hope it works')
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        subtitle = f'{post.subtitle}'
        image = f'{post.image}'
        author = f'{post.author}'
        content = f'{post.content}'
        self.assertEqual(author, 'Todun')
        self.assertEqual(title, 'Test title')
        self.assertEqual(subtitle, 'simple post')
        self.assertEqual(image, os.path.join(settings.BASE_DIR, 'media/posts_pics/header-img.png'))
        self.assertEqual(content, 'Hope it works')
