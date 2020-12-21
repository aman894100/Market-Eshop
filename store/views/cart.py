from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        # print(request.session.cart)
        cart = request.session.cart
        print(cart)
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        # print(products)
        return render(request, 'cart.html', {'products': products})
