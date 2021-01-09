from django.contrib.admin.utils import NestedObjects
from ..models import Category


def get_objects_for_category(category_slug):
    category = Category.objects.get(slug=category_slug)
    collector = NestedObjects(using='default')
    collector.collect([category])
    products = []
    for line in collector.data.values():
        products += line
    products = products[1:]
    return products


def get_product(category_slug, product_slug):
    category = Category.objects.get(slug=category_slug)
    products = get_objects_for_category(category.slug)
    for product in products:
        if product.slug == product_slug:
            return product


def get_all_products():
    models_amount = Category.objects.count()
    all_categorys = Category.objects.all()
    collector = NestedObjects(using='default')
    collector.collect(all_categorys)
    products = []
    for line in collector.data.values():
        products += line
    products = products[models_amount:]
    return products
