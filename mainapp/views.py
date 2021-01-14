from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.models import ContentType, User
from django.contrib import messages

from .forms import Registration
from .mixins import GetCategorysMixin, GetCurtMixin
from .models import Category, GlobalCategory, Customer, Cart, CartProduct
from .logic import get_products, cart_logic


class Index(GetCurtMixin, GetCategorysMixin, View):

    def get(self, request):
        products = get_products.get_all_products()[:6]
        context = {
            'products': products,
            'g_categorys': self.g_categorys,
            'cart': self.cart,
        }
        return render(request, 'index.html', context)


class ProductDetail(GetCurtMixin, GetCategorysMixin, View):

    def get(self, request, category_slug, product_slug):
        product = get_products.get_product(category_slug, product_slug)
        spec = get_products.get_product_specif(category_slug, product_slug)
        context = {
            'product': product,
            'g_categorys': self.g_categorys,
            'spec': spec,
            'cart': self.cart,
        }
        return render(request, 'product_detail.html', context)


class GlobalCategoryDetail(GetCurtMixin, GetCategorysMixin, View):

    def get(self, request, global_category_slug):
        g_category = GlobalCategory.objects.get(slug=global_category_slug)
        categorys = get_products.get_categorys_for_global_category(g_category.slug)
        products = []
        for category in categorys:
            products_for_category = get_products.get_objects_for_category(category.slug)
            products += products_for_category
        context = {
                'products': products,
                'g_categorys': self.g_categorys,
                'cart': self.cart,
        }
        return render(request, 'global_category_detail.html', context)


class CategoryDetail(GetCurtMixin, GetCategorysMixin, View):

    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        products = get_products.get_objects_for_category(category.slug)
        context = {
            'self_category': category,
            'products': products,
            'g_categorys': self.g_categorys,
            'cart': self.cart,
        }
        return render(request, 'category_detail.html', context)

class RegistrationView(View):

    def get(self, request):
        form = Registration
        context = {
                'form': form,
        }
        return render(request, 'registration//registration.html', context)

    def post(self, request):
        form = Registration(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            user = User.objects.create(username=username)
            user.set_password(password)
            user.customer.phone = phone
            user.customer.address = address
            user.save()
            messages.add_message(request, messages.INFO, 'Succefully register, now log in')
            return HttpResponseRedirect(reverse('login'))


class AddToCart(GetCurtMixin, View):

    def get(self, request, product_slug, category_slug):
        user = User.objects.get(username=request.user.username)
        customer = Customer.objects.get(user=user)
        category = Category.objects.get(slug=category_slug)
        product = get_products.get_product(category_slug=category.slug, product_slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(user=customer, to_cart=self.cart, 
                                                product_slug=product.slug, total_price=product.price,
                                                product_category=product.category.slug,
                                                )
        if created:
            self.cart.products.add(cart_product)
            self.cart.save()
        cart_logic.cart_recalc(self.cart)
        return HttpResponseRedirect(reverse('cart_detail'))


class CartView(GetCurtMixin, View):

    def get(self, request):
        context = {
            'cart': self.cart,
        }
        return render(request, 'cart_detail.html', context)


class DeleteCartProduct(GetCurtMixin, View):

    def get(self, request, cart_product_id):
        product = CartProduct.objects.get(id=cart_product_id)
        self.cart.products.remove(product)
        product.delete()
        cart_logic.cart_recalc(self.cart)
        return HttpResponseRedirect(reverse('cart_detail'))


class ChangeCartProductAmount(GetCurtMixin, View):

    def post(self, request, cart_product_id):
        product = CartProduct.objects.get(id=cart_product_id)
        amount = request.POST.get('amount')
        product.total_price = int(product.get_product().price) * int(amount)
        product.amount = amount
        product.save()
        cart_logic.cart_recalc(self.cart)
        return HttpResponseRedirect(reverse('cart_detail'))

