# Generated by Django 3.0.8 on 2020-11-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True, unique=True),
        ),
    ]