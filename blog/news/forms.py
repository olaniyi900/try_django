from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=200)
    author = forms.CharField(max_length=50)