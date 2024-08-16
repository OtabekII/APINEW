from django.urls import path, include
from Goods import views

urlpatterns = [
    path('', views.banner_view, name='banner_view'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
]