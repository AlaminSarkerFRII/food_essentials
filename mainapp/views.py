from django.shortcuts import render
from django.views import View
from .models import Products
from .forms import CustormerRegistrationForm,CustomerProfileForm
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

        return render(request, 'mainapp/custormer-registration-form.html', {'form' : form})


# class CustomerLoginView(View):
#     def get(self, request):
#         form = CustormerRegistrationForm()
#         return render(request, 'mainapp/login.html', locals())

    # def post(self, request):
    #     form = CustormerRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()


class CustomerProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,'mainapp/userprofile.html', locals())
    
    def post(self, request):
        return render(request,'mainapp/userprofile.html', locals())