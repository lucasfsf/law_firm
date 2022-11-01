from django.shortcuts import render
from django.db.models import Q

from .models import Article

from .company_fields import default_company_values

context = default_company_values

def index(request):
    # Main page 
    return render(request, 'articles/index.html', context)

def articles(request):
    # If Nothing was searched
    qs = Article.objects.order_by('-date_added')
    search_term = request.GET.get('q')
    if search_term is not None:
        # Something was searched
        lookups = Q(content__icontains=search_term) | Q(title__icontains=search_term)
        qs = Article.objects.filter(lookups).order_by('-date_added')

    context['articles'] = qs
    return render(request, 'articles/articles.html', context)

def article(request, slug):
    # Shows a single, full, article
    article = Article.objects.get(slug=slug)
    context['article'] = article

    return render(request, "articles/article.html", context)