# Generated by Django 3.1.7 on 2021-03-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0013_productincart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
