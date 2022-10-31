from django.test import TestCase

# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        for i in range(5):
            Article.objects.create(title='Test Title', content='blable', law_type='TR')
        self.articles = Article.objects.filter(title="Test Title")
        
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_slug_generation(self):
        for article in self.articles:
            self.assertIsNotNone(article.slug)

    def test_slugs_are_unique(self):
        self.assertEqual(len(self.articles), len(set(self.articles)))
        