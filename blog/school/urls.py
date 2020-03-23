from django.urls import path
from .views import (home,
    create_student,
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_student, name='craete'),
    path('student/', StudentListView.as_view(), name='students'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/new/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student_delete'),
]
