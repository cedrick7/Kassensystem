# Generated by Django 3.1.1 on 2020-09-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbox', '0003_auto_20200831_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_product',
            name='amount',
            field=models.IntegerField(default=50),
        ),
    ]
