from django.shortcuts import render
from django.views import View
from .models import Products
# Create your views here.


def home(request):
    return render(request, 'mainapp/index.html')


class CategoryView(View):

    def get(self, request, val):
        products = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title')
        return render(request, 'mainapp/category.html', locals())
        # locals() -is the built in function thats executes all variables pass
