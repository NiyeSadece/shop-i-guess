# Generated by Django 3.1.7 on 2021-03-26 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0018_auto_20210326_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='line1',
            new_name='apartment',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='line2',
            new_name='street',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='postcode',
            new_name='zip',
        ),
        migrations.RemoveField(
            model_name='address',
            name='phone',
        ),
    ]
