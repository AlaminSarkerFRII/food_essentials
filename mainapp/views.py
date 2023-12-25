from django.shortcuts import render
from django.views import View
# Create your views here.


def home(request):
    return render(request, 'mainapp/index.html')


class CategoryView(View):

    def get(self, request, val):
        # locals() -is the built in function thats executes all variables pass
        return render(request, 'mainapp/category.html', locals())
