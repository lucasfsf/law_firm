from django.shortcuts import render

from .models import Article

def index(request):
    # Main page 
    return render(request, 'articles/index.html')

def articles(request):
    articles = Article.objects.order_by('-date_added')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/articles.html', context)

def article(request, article_id):
    # Shows a single, full, article
    article = Article.objects.get(id=article_id)
    context = {
        "article": article,
    }
    return render(request, "articles/article.html", context)