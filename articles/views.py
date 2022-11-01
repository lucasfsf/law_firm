from django.shortcuts import render

from .models import Article

from .company_fields import default_company_values

context = default_company_values

def index(request):
    # Main page 
    return render(request, 'articles/index.html', context)

def articles(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)

    context['articles'] = qs
    return render(request, 'articles/articles.html', context)

def article(request, slug):
    # Shows a single, full, article
    article = Article.objects.get(slug=slug)
    context['article'] = article

    return render(request, "articles/article.html", context)