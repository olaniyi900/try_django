from django.urls import path
from . import views

urlpatterns = [
    path('',views.detail_post, name="detail_post"),
    path('<int:post_id>/', views.single_post, name="single_post"),
]
