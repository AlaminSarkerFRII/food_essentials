from django.db import models

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
