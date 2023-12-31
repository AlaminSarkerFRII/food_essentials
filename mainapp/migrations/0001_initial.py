# Generated by Django 4.2.6 on 2023-12-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_prices', models.FloatField()),
                ('discount_prices', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'Crud'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshek'), ('GH', 'Ghee'), ('PH', 'Pooner'), ('CZ', 'Cheese'), ('IC', 'Ice_cream')], max_length=2)),
                ('product_image', models.ImageField(upload_to='products_images/')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
