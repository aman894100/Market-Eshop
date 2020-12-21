from django.shortcuts import render, redirect, HttpResponseRedirect
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
        # import pdb;
        # pdb.set_trace()
        print(request.get_full_path()[1:])
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)







