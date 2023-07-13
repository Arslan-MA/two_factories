from django.shortcuts import render, get_object_or_404
from factory_2.models import Products2


def product_info(request, product_id):
    context = {"product": get_object_or_404(Products2, pk=product_id)}

    return render(request, 'product.html', context)
