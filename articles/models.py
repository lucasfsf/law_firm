from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    content = RichTextField()
    date_added = models.DateField(auto_now_add=True)

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

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
