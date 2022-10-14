from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Lawsuit

#TODO - add login required decorator

@login_required
def lawsuits(request):
    if request.user.is_authenticated:
        lawsuits = Lawsuit.objects.filter(customer=request.user)
        context = {
            "lawsuits": lawsuits,
        }
    else:
        return redirect("users:login")
    return render(request, "lawsuits/lawsuits.html", context)
