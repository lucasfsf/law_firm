from django.test import TestCase

# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 10
        for i in range(self.number_of_articles):
            Article.objects.create(title='Test Title', content='blable', law_type='TR')
        self.articles = Article.objects.filter(title="Test Title")
        
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
    
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

    def test_slug_generation(self):
        for article in self.articles:
            self.assertIsNotNone(article.slug)

    def test_slugs_are_unique(self):
        self.assertEqual(len(self.articles), len(set(self.articles)))

    def test_first_slug(self):
        qs = Article.objects.all().first()
        self.assertEqual(qs.slug, 'test-title')
    
    def test_last_slug(self):
        qs = Article.objects.all().last()
        qs_slug = f'test-title-{self.number_of_articles}'
        self.assertEqual(qs.slug, qs_slug)
        