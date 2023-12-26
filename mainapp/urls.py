from django.urls import path
from .views import home, CategoryView, ProductDetails, CategoryTitleView


urlpatterns = [
    path('', home, name='home'),
    path('category-title/<val>', CategoryTitleView.as_view(), name='category-title'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('product-details/<int:pk>',
         ProductDetails.as_view(), name='product-details'),
]
