from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    date_added = models.DateField(auto_now_add=True)

    #Law Choices
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
        (CONSTITUTIONAL, "Constitucional"),
        (TAX, "Tributário"),
        (CIVIL, "Civil"),
        (ADMINISTRATIVE, "Administrativo"),
        (CRIMINAL, "Criminal"),
        (CORPORATE, "Empresarial"),
        (FAMILY, "de Familia"),
        (LABOR, "Trabalhista"),
        (OTHERS, "(Outros)"),
    ]

    law_type = models.CharField(max_length=2, 
        choices=TRIBUTARY_LAW_CHOICES, 
        default=OTHERS,
        )

    def __str__(self):
        return self.title
