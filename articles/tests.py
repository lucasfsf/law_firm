from django.test import TestCase
from django.utils.text import slugify

# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 10
        self.article_title = 'Test Title'
        self.slugified_title = slugify(self.article_title)
        for i in range(self.number_of_articles):
            Article.objects.create(title=self.article_title, content='blable', law_type='TR')
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
        qs = Article.objects.all().order_by('id').first()
        self.assertEqual(qs.slug, self.slugified_title)
    
    def test_last_slug(self):
        qs = Article.objects.all().order_by('id').last()
        qs_slug = f'{self.slugified_title}-{self.number_of_articles}'
        self.assertEqual(qs.slug, qs_slug)

    def test_article_search_with_query(self):
        Article.objects.create(title="Searchable", content='blable', law_type='TR')
        qs = Article.objects.search("searchable")
        self.assertEqual(len(qs), 1)
    
    def test_article_search_empty(self):
        qs = Article.objects.search("")
        self.assertEqual(len(qs), self.number_of_articles)

    def test_article_search_none(self):
        qs = Article.objects.search(None)
        self.assertEqual(len(qs), self.number_of_articles)
        