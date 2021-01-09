from django.urls import path
from .views import Index, ProductDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:category_slug>/<str:product_slug>/', ProductDetail.as_view(), name='product_detail'),
]
