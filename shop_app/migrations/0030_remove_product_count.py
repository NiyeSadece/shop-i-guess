# Generated by Django 3.1.7 on 2021-03-27 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0029_auto_20210327_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
    ]
