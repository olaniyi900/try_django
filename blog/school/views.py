from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    qs = Student.objects.all()
    template_name = 'school/home.html'
    context = {
        'students':qs
    }
    return render(request, template_name, context)
