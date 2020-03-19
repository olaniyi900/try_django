from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    title = "This is index page"
    context = {"title":title}
    return render(request, "index.html", context)