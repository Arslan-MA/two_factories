from django.shortcuts import render
from factory_1.models import Products1
from factory_2.models import Products2


def all_content(request):
    context = {"products_1": Products1.objects.all(),
               "products_2": Products2.objects.all()}

    return render(request, "allProducts.html", context)


def product_info(request, product_id):
    context = {"product": Products1.objects.get(id=product_id)}

    return render(request, 'product.html', context)
