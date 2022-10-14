from django.shortcuts import render, redirect

from .models import Lawsuit

def lawsuits(request):
    if request.user.is_authenticated:
        lawsuits = Lawsuit.objects.filter(customer=request.user)
        context = {
            "lawsuits": lawsuits,
        }
    else:
        return redirect("users:login")
    return render(request, "lawsuits/lawsuits.html", context)
