from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Lawsuit, Movement


@login_required
def lawsuits(request):
    context = {}
    if request.user.is_authenticated:
        lawsuits = Lawsuit.objects.filter(customer=request.user)
        context = {
            "lawsuits": lawsuits,
        }

    return render(request, "lawsuits/lawsuits.html", context)

def movement(request, lawsuit_id):
    # Shows a single, full, article
    lawsuit = Lawsuit.objects.get(id=lawsuit_id)
    movements = Movement.objects.filter(lawsuit=lawsuit).order_by('-date_added')
    context = {
        "movements": movements,
        "lawsuit": lawsuit,
    }
    return render(request, "lawsuits/movement.html", context)