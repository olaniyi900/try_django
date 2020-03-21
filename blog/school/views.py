from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentModelForm


# Create your views here.

def home(request):
    qs = Student.objects.all()
    template_name = 'school/home.html'
    context = {
        'students':qs
    }
    return render(request, template_name, context)


def create_student(request):
    form = StudentModelForm(request.POST)
    if form.is_valid():
        #unpack the dictinary for forms.Form
        # by using Student.objects.create(**form.cleaned_data)
        form.save() #use save for modelform
        print(form.cleaned_data)
        form = StudentModelForm()
        return redirect('/schools/')
    template_name = 'school/create.html'
    context = {
        "form": form
    }
    return render(request, template_name, context)
