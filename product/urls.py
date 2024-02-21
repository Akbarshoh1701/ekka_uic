from product.views import ProductView, ProductDetailView
from django.urls import path

urlpatterns = [
        path('product/', ProductView.as_view(), name='product'),
        path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail')
]