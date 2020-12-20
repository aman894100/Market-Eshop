from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from django.utils.decorators import  method_decorator
# from store.middlewares.auth import auth_middleware



class Orders(View):
    # # if a middleware is called for any normal function then we have to call it like: @middleware_name
    # # but since here it is a mthod or instance of a class Orders we have impport it first and then call it like:
    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})