from django.urls import path
from .views import (home,
    create_student,
    StudentListView,
    StudentDetailView

)

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_student, name='craete'),
    path('student/', StudentListView.as_view(), name='students'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
