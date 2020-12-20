from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# print(make_password('1242'))
# print(check_password('1242','pbkdf2_sha256$216000$8CV5jrHrGfFo$Qsjid7KRw2uwSopUraZWlOTsN/jCOeGpCOvm/YKcDCs='
# ))




class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        email = postdata.get('email')
        password = postdata.get('password')
        phone = postdata.get('phone')
        value = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone}

        # creation of a customer
        customer = Customer(email=email, first_name=first_name, last_name=last_name, password=password, phone=phone)
        error_msg = self.validateCustomer(customer)

        # if form is valid
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            # valid_msg = "Registration succeed"
            return redirect('homepage')
        else:
            data = {'errors': error_msg, 'values': value}
            return render(request, 'signup.html', data)

    # validation of form data
    def validateCustomer(self, customer):
        error_msg = None
        if not customer.first_name:
            error_msg = "First name is required!"
        elif len(customer.first_name) > 10:
            error_msg = "First name can not be more than 10 characters!"
        elif not customer.last_name:
            error_msg = "Last name is required!"
        elif len(customer.last_name) > 10:
            error_msg = "Last name can not be more than 10 characters!"
        elif not customer.password:
            error_msg = "Password is required!"
        elif len(customer.password) < 4:
            error_msg = "Password length should be greater than 4 characters"
        elif not customer.phone:
            error_msg = "Phone number is required!"
        elif len(customer.phone) > 10:
            error_msg = "Phone number can not be more than 10 characters!"
        elif customer.is_exist():
            error_msg = "Email is already taken"

        return error_msg
