from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    title = "This is index page"
    context = {"title":title, "frd_list": ["Ade", "Sandra", "Comfort"]}
    if request.user.is_authenticated:
        context = {"title":title, "name": request.user, "frd_list": ["Ade", "Sandra", "Comfort"]}
    return render(request, "index.html", context)


def about(request):
    title = "This is about us page"
    context = {"title":title}
    return render(request, "about.html", context)