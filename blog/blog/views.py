from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm

def index(request):
    title = "This is index page"
    context = {"title":title, "frd_list": ["Ade", "Sandra", "Comfort"]}
    if request.user.is_authenticated:
        context = {"title":title, "name": request.user, "frd_list": ["Ade", "Sandra", "Comfort"]}
    return render(request, "index.html", context)


def about(request):
    #print(request.POST["name"])
    form = PostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    form = PostForm()

    title = "This is about us page"
    context = {"title":title, "form":form}
    return render(request, "about.html", context)