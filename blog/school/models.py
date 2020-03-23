from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    