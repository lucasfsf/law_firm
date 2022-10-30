from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Lawsuit, Movement

from articles.company_fields import default_company_values

context = default_company_values

@login_required
def lawsuits(request):
    if request.user.is_authenticated:
        lawsuits = Lawsuit.objects.filter(customer=request.user)
        context["lawsuits"] = lawsuits
        print(context)


    return render(request, "lawsuits/lawsuits.html", context)

def movement(request, lawsuit_id):
    # Shows a single, full, article
    lawsuit = Lawsuit.objects.get(id=lawsuit_id)
    # If user is not the owner of the lawsuit, redirect to lawsuits
    if request.user not in lawsuit.customer.all():
        return redirect("lawsuits:lawsuits")
        
    movements = Movement.objects.filter(lawsuit=lawsuit).order_by('-date_added')
    context["movements"] = movements
    context["lawsuit"] = lawsuit

    return render(request, "lawsuits/movement.html", context)