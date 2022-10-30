from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['law_type', 'title', 'slug']
    search_fields = ['law_type', 'title', 'content']

admin.site.register(Article, ArticleAdmin)