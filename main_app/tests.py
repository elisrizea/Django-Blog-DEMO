# Create your tests here.

# ********************** end url test *************************************

# ************* test views *****************
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Posts
from .serializers import PostSerializer


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_portfolio_view(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio.html')

    def test_posts_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_add_post_view(self):
        self.client.login(username='test1', password='password can’t be')
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

        response = self.client.post(reverse('add_post'), {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'post_author': 'test',
        })
        #self.assertEqual(response.status_code, 200)
        #self.assertRedirects(response, reverse('posts'))

        post = Posts.objects.get(title='Test Post')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')
        self.assertEqual(post.post_author, 'test')

    def test_add_post_view_unauthenticated(self):
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Only loged in user are allowd to add posts')




class PostApiViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)


# ************* test model*****************
from django.test import TestCase
from .models import Posts


class PostsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Posts.objects.create(
            post_author='Test Author',
            title='Test Title',
            content='Test Content'
        )

    def test_post_author_label(self):
        post = Posts.objects.get(id=1)
        field_label = post._meta.get_field('post_author').verbose_name
        self.assertEqual(field_label, 'post author')

    def test_title_label(self):
        post = Posts.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_content_label(self):
        post = Posts.objects.get(id=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_date_label(self):
        post = Posts.objects.get(id=1)
        field_label = post._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_post_author_max_length(self):
        post = Posts.objects.get(id=1)
        max_length = post._meta.get_field('post_author').max_length
        self.assertEqual(max_length, 150)

    def test_title_max_length(self):
        post = Posts.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 150)

    def test_content_max_length(self):
        post = Posts.objects.get(id=1)
        max_length = post._meta.get_field('content').max_length
        self.assertEqual(max_length, None)

    def test_date_not_null(self):
        post = Posts.objects.get(id=1)
        date_null = post._meta.get_field('date').null
        self.assertEqual(date_null, False)

    def test_post_author_not_null(self):
        post = Posts.objects.get(id=1)
        post_author_null = post._meta.get_field('post_author').null
        self.assertEqual(post_author_null, False)

    def test_title_not_null(self):
        post = Posts.objects.get(id=1)
        title_null = post._meta.get_field('title').null
        self.assertEqual(title_null, False)

    def test_content_not_null(self):
        post = Posts.objects.get(id=1)
        content_null = post._meta.get_field('content').null
        self.assertEqual(content_null, False)


# ************************************

