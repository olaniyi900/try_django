from django.forms import ModelForm
from .models import Product

class ProductCreateForm(ModelForm):

    
    class Meta:
        model = Product
        fields = ['name', 'description','quantity', 'price']
    


