# Generated by Django 3.0.8 on 2020-10-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20201018_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, unique=True),
        ),
    ]
