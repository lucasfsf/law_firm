from django.shortcuts import render

from .models import Article

def index(request):
    # Main page 
    return render(request, 'articles/index.html')

def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/articles.html', context)