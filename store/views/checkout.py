from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer


class Checkout(View):
    def get(self,request):
        return redirect('cart')

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, products)

        # iteration over products to save each order having a particular product object
        for product in products:
            order = Order(address = address,
                          phone = phone,
                          customer = Customer(id = customer),
                          product = product,
                          quantity = cart.get(str(product.id)),
                          price = product.price)
            order.placeOrder()
        # for clearing cart after placing the orders
        request.session['cart'] = {}

        return redirect('cart')
