from django.shortcuts import render, redirect, HttpResponseRedirect
# HttpResponseRedirect is normally used to redirect to a specific url that we are getting by request.get method
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View



class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        # print(customer)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                # for storing the customer info in session
                print(customer)
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_msg = "Email or Password is invalid!"
        else:
            error_msg = "Email or Password is invalid!"

        return render(request, 'login.html', {'errors': error_msg})
