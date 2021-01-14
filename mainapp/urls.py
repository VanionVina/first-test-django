from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    Index, ProductDetail, 
    GlobalCategoryDetail,
    CategoryDetail,
    RegistrationView)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<str:category_slug>/<str:product_slug>/', ProductDetail.as_view(), name='product_detail'),
    path('global/<str:global_category_slug>/', GlobalCategoryDetail.as_view(), name='global_category_detail'),
    path('not-global/<str:category_slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
