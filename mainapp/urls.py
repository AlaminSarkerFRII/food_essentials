from django.urls import path
from .views import home, about, contact, CategoryView, ProductDetails, CategoryTitleView


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category-title/<val>', CategoryTitleView.as_view(), name='category-title'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('product-details/<int:pk>',
         ProductDetails.as_view(), name='product-details'),
]
