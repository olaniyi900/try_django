from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentModelForm
from django.views.generic import (ListView, 
                DetailView, 
                CreateView, 
                UpdateView,
                DeleteView)


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


# class base view to list all the object in the data base
class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'age']


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'age']

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    