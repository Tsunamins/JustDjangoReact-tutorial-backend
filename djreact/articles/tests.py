from django.test import TestCase
from django.test import TestCase
from .models import Article

from rest_framework.test import APIClient
from rest_framework import status
# from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.article_title = "Write world class code"
        self.article = Article(title=self.article_title)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Article.objects.count()
        self.article.save()
        new_count = Article.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.article_data = {'title': 'Go to Ibiza', 'content': 'New article from tests'}
        self.response = self.client.post('/api/create/', self.article_data, format='json')
        # self.assertEqual(response.status_code, 201)

        # self.response = self.client.post(
        #     '/api/create/',
        #     self.article_data,
        #     format="json")

    def test_api_can_create_a_article(self):
        """Test the api has article creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
