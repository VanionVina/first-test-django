from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import ContentType


from .models import Category, GlobalCategory
from .logic import get_products


class Index(View):

    def get(self, request):
        products = get_products.get_all_products()[:6]
        global_categorys = GlobalCategory.objects.all()
        context = {
            'products': products,
            'global_categorys': global_categorys,
        }
        return render(request, 'index.html', context)

class ProductDetail(View):

    def get(self, request, category_slug, product_slug):
        product = get_products.get_product(category_slug, product_slug)
        global_categorys = GlobalCategory.objects.all()
        context = {
            'product': product,
            'global_categorys': global_categorys,
        }
        return render(request, 'product_detail.html', context)
