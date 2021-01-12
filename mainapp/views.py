from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import ContentType


from .mixins import GetCategorysMixin
from .models import Category, GlobalCategory
from .logic import get_products


class Index(GetCategorysMixin, View):

    def get(self, request):
        products = get_products.get_all_products()[:6]
        context = {
            'products': products,
            'g_categorys': self.g_categorys,
        }
        return render(request, 'index.html', context)


class ProductDetail(GetCategorysMixin, View):

    def get(self, request, category_slug, product_slug):
        product = get_products.get_product(category_slug, product_slug)
        spec = get_products.get_product_specif(category_slug, product_slug)
        context = {
            'product': product,
            'g_categorys': self.g_categorys,
            'spec': spec,
        }
        return render(request, 'product_detail.html', context)


class GlobalCategoryDetail(GetCategorysMixin, View):

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
        }
        return render(request, 'global_category_detail.html', context)


class CategoryDetail(GetCategorysMixin, View):

    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        products = get_products.get_objects_for_category(category.slug)
        context = {
            'self_category': category,
            'products': products,
            'g_categorys': self.g_categorys,
        }
        return render(request, 'category_detail.html', context)
