from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Products, Customer, CartItem
from .forms import CustormerRegistrationForm, CustomerProfileForm
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


class CategoryView(View):

    def get(self, request, val):
        products = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title')
        return render(request, 'mainapp/category.html', locals())
        # locals() -is the built in function thats executes all variables pass


class CategoryTitleView(View):

    def get(self, request, val):
        products = Products.objects.filter(title=val)
        title = Products.objects.filter(
            category=products[0].category).values('title')

        return render(request, 'mainapp/category.html', locals())


class ProductDetails(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        return render(request, 'mainapp/product-details.html', locals())


# <======================> Authentication <======================>


class CustomerRegistrationView(View):

    def get(self, request):
        form = CustormerRegistrationForm()
        return render(request, 'mainapp/custormer-registration-form.html', locals())

    def post(self, request):
        form = CustormerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulatons !! User Regitrations Successfull")
        else:
            messages.error(request, "Invalid Input Data")

        return render(request, 'mainapp/custormer-registration-form.html', {'form': form})


# class CustomerLoginView(View):
#     def get(self, request):
#         form = CustormerRegistrationForm()
#         return render(request, 'mainapp/login.html', locals())

# def post(self, request):
#     form = CustormerRegistrationForm(request.POST)
#     if form.is_valid():
#         form.save()


class PasswordChangeView(View):
    pass


class PasswordChangeDoneView(View):
    pass


class CustomerProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'mainapp/userprofile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)

        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            identity = form.cleaned_data['identity']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, identity=identity, city=city, mobile=mobile, state=state,
                           zipcode=zipcode)

            reg.save()
            messages.success(request, "Congratulations ! you have successfully save profile")
        else:
            messages.warning(request, "Invalid profile Data")

        return render(request, 'mainapp/userprofile.html', locals())


def address(request):
    address = Customer.objects.filter(user=request.user)

    return render(request, 'mainapp/address.html', locals())


# UpdateAddress

class UpdateAddress(View):

    def get(self, request, pk):
        address = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=address)
        return render(request, 'mainapp/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            address = Customer.objects.get(pk=pk)
            address.name = form.cleaned_data['name']
            address.identity = form.cleaned_data['identity']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.mobile = form.cleaned_data['mobile']
            address.zipcode = form.cleaned_data['zipcode']

            address.save()
            messages.success(request, "Congratulations ! you have successfully Updated Address !!")
        else:
            messages.warning(request, "Invalid Address!")

        return redirect('address')

    # ================= Add To Cart =======================> 


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Products.objects.get(id=product_id)

    CartItem.objects.create(user=user, products=product)

    return redirect('/cart-view')


def cart_view(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.products.discount_prices for item in cart_items)
    return render(request, 'mainapp/addtocart.html', locals())
