# Generated by Django 4.1 on 2022-09-14 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0028_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
