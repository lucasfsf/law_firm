from django.shortcuts import render

from .models import Article

from .company_fields import default_company_values

context = default_company_values

def index(request):
    # Main page 
    return render(request, 'articles/index.html', context)

def articles(request):
    # Checks if something was searched
    if not request.GET:
        # Nothing was searched
        articles = Article.objects.order_by('-date_added')
    else:
        search_term = request.GET['q']
        articles = Article.objects.filter(content__icontains=search_term).order_by('-date_added')
    context['articles'] = articles
    return render(request, 'articles/articles.html', context)

def article(request, article_id):
    # Shows a single, full, article
    article = Article.objects.get(id=article_id)
    context['article'] = article

    return render(request, "articles/article.html", context)