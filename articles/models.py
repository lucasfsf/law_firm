from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
