from django.db import models


def cart_recalc(cart):
    cart_info = cart.products.aggregate(models.Sum('total_price'))
    cart_amount = cart.products.count()
    cart.final_price = cart_info.get('total_price__sum')
    cart.final_amount = cart_amount
    cart.save()
