# blog/tests.py

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='farzi@kaka.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title="Great Game",
            body="Lovely Game mdt",
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual('{}'.format(self.post.title), 'Great Game')
        self.assertEqual('{}'.format(self.post.author), 'testuser')
        self.assertEqual('{}'.format(self.post.body), 'Lovely Game mdt')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lovely Game mdt')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/1001')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(no_response.status_code, 301)
        import pdb; pdb.set_trace()
        # self.assertContains(response, "Great Game")
        # self.assertTemplateUsed(response, 'post_detail.html')
