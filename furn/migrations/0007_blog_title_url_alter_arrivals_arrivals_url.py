# Generated by Django 4.0.6 on 2022-07-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title_url',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arrivals',
            name='arrivals_url',
            field=models.URLField(max_length=500),
        ),
    ]
