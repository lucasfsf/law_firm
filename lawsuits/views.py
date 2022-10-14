from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Lawsuit


@login_required
def lawsuits(request):
    context = {}
    if request.user.is_authenticated:
        lawsuits = Lawsuit.objects.filter(customer=request.user)
        context = {
            "lawsuits": lawsuits,
        }

    return render(request, "lawsuits/lawsuits.html", context)
