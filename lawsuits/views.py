from django.shortcuts import render

from .models import Lawsuit

def lawsuits(request):
    #TODO - Only display lawsuits that belong to a specific user
    lawsuits = Lawsuit.objects.all()
    print(lawsuits)
    context = {
        "lawsuits": lawsuits,
    }
    return render(request, "lawsuits/lawsuits.html", context)
