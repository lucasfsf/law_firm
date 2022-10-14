from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
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
        (CORPORATE, "Corporativo"),
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
