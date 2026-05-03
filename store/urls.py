from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),

    # Product detail page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Add to cart
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # Cart page
    path('cart/', views.cart_view, name='cart_view'),

    # checkout page
    path('checkout/', views.checkout, name='checkout'),
]

