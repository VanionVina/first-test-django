from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    Index, ProductDetail, 
    GlobalCategoryDetail,
    CategoryDetail,
    RegistrationView,
    AddToCart,
    CartView,
    DeleteCartProduct,
    ChangeCartProductAmount,
    )


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<str:category_slug>/<str:product_slug>/', ProductDetail.as_view(), name='product_detail'),
    path('global/<str:global_category_slug>/', GlobalCategoryDetail.as_view(), name='global_category_detail'),
    path('not-global/<str:category_slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add-to-cart/<str:product_slug>/<str:category_slug>/', AddToCart.as_view(), name='add_to_cart'),
    path('cart-detail/', CartView.as_view(), name='cart_detail'),
    path('del-cart-product/<str:cart_product_id>/', DeleteCartProduct.as_view(), name='del_cart_product'),
    path('change-amount/<str:cart_product_id>/', ChangeCartProductAmount.as_view(), name='change_amount'),
]
