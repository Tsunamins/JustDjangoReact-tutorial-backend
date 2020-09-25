from django.test import TestCase
from .models import Article

from rest_framework.test import APIClient
from rest_framework import status

from rest_framework.test import force_authenticate

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
  

    def test_api_can_create_a_article(self):
        """Test the api has article creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_article(self):
        """Test the api can get a given bucketlist."""
        article = Article.objects.get()
      
        response = self.client.get('/api/{}'.format(article.id), format="json")
        # reverse('details',
        # kwargs={'pk': article.id}), format="json"

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, article)

    def test_api_can_update_article(self):
        """Test the api can update a given bucketlist."""
        article = Article.objects.get()
      
        change_article = {'title': 'An article to update', 'content': 'Updated article content'}
      
        res = self.client.put('/api/{}/update/'.format(article.id), change_article, format="json")
        #     reverse('details', kwargs={'pk': article.id}),
        #     change_article, format='json'
        # )
      
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_article(self):
        """Test the api can delete a bucketlist."""
        article = Article.objects.get()
      
        response = self.client.delete('/api/{}/delete/'.format(article.id), format="json", follow=True)
        # reverse('details', kwargs={'pk': article.id}),
        # format='json',
        # follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
