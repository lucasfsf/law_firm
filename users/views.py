from django.shortcuts import render

def dashboard(request):
    # Shows info about a specific user
    return render(request, "users/dashboard.html")