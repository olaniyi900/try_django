from django.urls import path
from . import views

urlpatterns = [
    path('',views.detail_post, name="detail_post"),
    path('create/',views.create_post, name="create"),
    path('<int:post_id>/', views.single_post, name="single_post"),
]
