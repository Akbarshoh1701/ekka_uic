from product.views import *
from django.urls import path
from product.views import ShopListView, ShopDetailView

urlpatterns = [
    path('ShopListView/', ShopListView.as_view(), name='Product'),
    path('product/<int:pk>/', ShopDetailView.as_view(), name='product-detail')
]
