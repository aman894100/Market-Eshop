
from django.contrib import admin
from django.urls import path
from store.views.home import Index
from store.views.login import Login
from store.views.signup import Signup
from store.views.logout import logout
from store.views.cart import Cart
from store.views.checkout import Checkout
from store.views.orders import Orders
from store.middlewares.auth import auth_middleware



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', auth_middleware(Checkout.as_view()), name='checkout'),
    path('orders', auth_middleware(Orders.as_view()), name='orders'),

]
