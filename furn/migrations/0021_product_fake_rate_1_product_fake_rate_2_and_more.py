# Generated by Django 4.1 on 2022-09-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0020_contact_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fake_rate_1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='fake_rate_2',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='product',
            name='fake_rate_3',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='product',
            name='fake_rate_4',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='product',
            name='fake_rate_5',
            field=models.IntegerField(default=5),
        ),
    ]
