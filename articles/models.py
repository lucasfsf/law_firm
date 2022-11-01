from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.db.models import Q


class ArticleManager(models.Manager):
    def search(self, query=None):
        if query is None or query == "":
            # Nothing was searched
            lookups = Q()
        else:
            # Something was searched
            lookups = Q(content__icontains=query) | Q(title__icontains=query)
        return Article.objects.filter(lookups).order_by('-date_added')

class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True, max_length=150)
    content = RichTextField()
    date_added = models.DateField(auto_now_add=True)

    objects = ArticleManager()

    #Law Choices
    # TODO You might want to update the values below to add new types of law or to translate them.
    # If you add new types of law, you need to update the TRIBUTARY_LAW_CHOICES below to include the info
    CONSTITUTIONAL = "CO"
    TAX = "TR"
    CIVIL = "CI"
    ADMINISTRATIVE = "AD"
    CRIMINAL = "CR"
    CORPORATE = "CP"
    FAMILY = "FA"
    LABOR = "LA"
    OTHERS = "OT"

    TRIBUTARY_LAW_CHOICES = [
        (CONSTITUTIONAL, "Constitutional"),
        (TAX, "Tax"),
        (CIVIL, "Civil"),
        (ADMINISTRATIVE, "Administrative"),
        (CRIMINAL, "Criminal"),
        (CORPORATE, "Corporate"),
        (FAMILY, "Family"),
        (LABOR, "LAbor"),
        (OTHERS, "(Other)"),
    ]

    law_type = models.CharField(max_length=2, 
        choices=TRIBUTARY_LAW_CHOICES, 
        default=OTHERS,
        )

    def __str__(self):
        return self.title

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
            slugified_url = slugify(instance.title)
            # check if it already exists
            qs = Article.objects.filter(slug__contains=slugified_url).exclude(id=instance.id)
            if qs.exists():
                # slug url already being used by another article
                slugified_url = f'{slugified_url}-{qs.count() + 1}'            
            instance.slug = slugified_url

# Connecting article_pre_save to pre_save SIGNAL
pre_save.connect(article_pre_save, sender=Article)