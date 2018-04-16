from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="Test for testing")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_value = '{0}'.format(post.text)
        self.assertEqual(expected_value, 'Test for testing')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text="Another text for testing")

    def test_url_by_location(self):
        resp = self.client.get('/')
        # import pdb; pdb.set_trace()
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
