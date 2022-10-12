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