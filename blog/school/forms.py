from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     age = forms.IntegerField()

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"