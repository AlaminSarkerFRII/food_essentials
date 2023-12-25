from django.urls import path
from .views import home, CategoryView, ProductDetails


urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('product-details/<int:pk>',
         ProductDetails.as_view(), name='product-details'),
]
