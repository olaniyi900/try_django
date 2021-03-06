from django.shortcuts import render, get_object_or_404

from .models import NewsPost
from .forms import PostForm

# Create your views here.

def detail_post(request):
    obj = NewsPost.objects.all()
    template_name = "detail_post.html"
    context = {"newspost": obj}
    return render(request, template_name, context)


def single_post(request, post_id):
    #obj = NewsPost.objects.get(id=post_id)
    obj = get_object_or_404(NewsPost, id=post_id)
    template_name = "single_post.html"
    context = {"newspost": obj}
    return render(request, template_name, context)


def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        obj = NewsPost.objects.create(**form.cleaned_data)
        
        form = PostForm()
    template_name = "create.html"
    context = {"form": form}
    return render(request, template_name, context)
