from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, register, login_view

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),  
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),  
    

    path('categorys/', CategoryList.as_view(), name='category-list'),  
    path('categorys/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),  


    path('register/', register, name='register'), 
    path('login/', login_view, name='login'),  
]
