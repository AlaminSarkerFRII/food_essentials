from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CHOISE_CATEGORIES = [
    ('CR', 'Crud'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshek'),
    ('GH', 'Ghee'),
    ('PH', 'Pooner'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice_cream'),
]

STATE_LISTS = [

    ('DH', 'Dhaka'),
    ('RG', 'Rangpur'),
    ('RJ', 'Rajshahi'),
    ('MS', 'Maymonsing'),
    ('BL', 'Barishal'),
    ('SL', 'Syhlet'),
    ('CTG', 'Chattogram'),
    ('KH', 'Khulna'),
]


class Products(models.Model):
    title = models.CharField(max_length=100)
    selling_prices = models.FloatField()
    discount_prices = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CHOISE_CATEGORIES, max_length=2)
    product_image = models.ImageField(upload_to='products_images/')

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    identity = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    mobile = models.IntegerField(default=0)
    state = models.CharField(choices=STATE_LISTS, max_length=100)
    zipcode = models.IntegerField()

        
    def __str__(self):
        return f"{self.name} {self.user}"

