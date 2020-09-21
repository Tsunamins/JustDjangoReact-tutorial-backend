from django.test import TestCase
from django.test import TestCase
from .models import Article


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


