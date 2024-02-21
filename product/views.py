from django.shortcuts import render
from django.views import View
from product.forms import CommentForm
from product.models import Product, Category, Size, Color


class ProductView(View):
    def get(self, request):
        context = {
            'product': Product.objects.all(),
            'category': Category.objects.all(),
            'size': Size.objects.all(),
            'color': Color.objects.all(),
        }
        return render(request, 'product_list.html', context)


class ProductDetailView(View):
    def get(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = CommentForm()
        context = {
            'product': Product.objects.get(slug=slug)
        }
        return render(request, 'product-details.html', context)



