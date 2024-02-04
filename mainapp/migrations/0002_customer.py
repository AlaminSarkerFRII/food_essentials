# Generated by Django 4.2.6 on 2024-01-02 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('identity', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('mobile', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('DH', 'Dhaka'), ('RG', 'Rangpur'), ('RJ', 'Rajshahi'), ('MS', 'Maymonsing'), ('BL', 'Barishal'), ('SL', 'Syhlet'), ('CTG', 'Chattogram'), ('KH', 'Khulna')], max_length=100)),
                ('zipcode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]