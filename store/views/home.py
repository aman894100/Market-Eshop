from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    # for handling the product id coming from the form html whenever clicked on add to cart button
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # import pdb;pdb.set_trace()

        # if the cart is already store in the session of a customer
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:

                cart[product] = 1
            print(quantity)
        else:
            cart = {}
            cart[product] = 1
            # for creation of cart if there is no cart active whenever we land to hompage
            request.session['cart'] = cart
            
        # for updating the cart of a user in user's session
        request.session['cart'] = cart
        print('cart:' , request.session['cart'])
        return redirect('homepage')


    def get(self, request):
        # whenever homepage reloads in index.html it will look for cart first. so we have to create cart first if it is
        # not there and if cart is already present then just get it from session
        cart = request.session.get('cart', 'CART NOT FOUND')
        if not cart:
            request.session['cart'] = {}

        categories = Category.get_all_categories()
        # print(request.GET)
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_categoryid(category_id)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are: ', request.session.get('email'))
        return render(request, 'index.html', data)






