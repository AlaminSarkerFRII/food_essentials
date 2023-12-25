from django.urls import path
from .views import home, CategoryView


urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
]
