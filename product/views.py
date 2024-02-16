from django.shortcuts import render
from django.views.generic import View

from product.models import Product, Size, Category, Color, ProductImage


# Create your views here.


class ShopListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "product_ls": Product.objects.all(),
            "size_ls": Size.objects.all(),
            "categories": Category.objects.all(),
            "color": Color.objects.all(),
            "product_image": ProductImage.all()
        }
        return render(request, 'product_list.html', context)

class ShopDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        context = {
            'product': product
        }
        return render(request, 'product-details.html', context)

