from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.

def home(request):
    qs = Student.objects.all()
    template_name = 'school/home.html'
    context = {
        'students':qs
    }
    return render(request, template_name, context)


def create_student(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        obj = Student.objects.create(**form.cleaned_data)
        print(form.cleaned_data)
        form = StudentForm()
        return redirect('/schools/')
    template_name = 'school/create.html'
    context = {
        "form": form
    }
    return render(request, template_name, context)
