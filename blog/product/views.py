from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreateForm

def productHome(request):
    qs = Product.objects.all()
    context = {
        'products': qs
    }
    template_name = 'product/producthome.html'
    return render(request, template_name, context)


def product_detail(request, p_id):
    qs = Product.objects.get(id=p_id)
    template_name = 'product/product_detail.html'
    context = {
        'product':qs
    }
    return render(request, template_name, context)


def product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            
            Product.objects.create(**form.cleaned_data)
            return redirect('product_home')
    
    form = ProductCreateForm()
    
    template_name = 'product/product_create.html'
    context = {'form': form}
        
    return render(request, template_name, context)

def product_update(request, p_id):
    product = Product.objects.get(pk=p_id)
    if request.method == 'POST':
       
        form = ProductCreateForm(request.POST, instance=product)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('product_home')

    
    form = ProductCreateForm(instance=product)
    
    template_name = 'product/product_create.html'
    context = {'form': form}
        
    return render(request, template_name, context)