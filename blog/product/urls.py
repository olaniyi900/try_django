from django.urls import path
from . import views

urlpatterns = [
    path('', views.productHome, name='product_home'),
    path('detail/<int:p_id>/', views.product_detail, name='product_detail'),
    path('update/<int:p_id>/', views.product_update, name='product_update'),
    path('delete/<int:p_id>/', views.product_delete, name='product_delete'),
    path('add/', views.product_create, name='product_create'),
]