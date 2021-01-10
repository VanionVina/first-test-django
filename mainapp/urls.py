from django.urls import path
from .views import Index, ProductDetail, GlobalCategoryDetail, CategoryDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:category_slug>/<str:product_slug>/', ProductDetail.as_view(), name='product_detail'),
    path('<str:global_category_slug>/', GlobalCategoryDetail.as_view(), name='global_category_detail'),
    path('x/x/<str:category_slug>/', CategoryDetail.as_view(), name='category_detail')
]
