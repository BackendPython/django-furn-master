# Generated by Django 4.1 on 2022-09-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0022_rename_fake_rate_1_product_rate_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rate_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rate_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rate_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rate_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rate_5',
        ),
        migrations.AddField(
            model_name='product',
            name='rate_1_choices',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, max_length=8),
        ),
    ]
