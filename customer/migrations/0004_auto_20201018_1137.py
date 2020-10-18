# Generated by Django 3.0.8 on 2020-10-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20201017_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='details',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phonenumber',
            field=models.DecimalField(blank=True, decimal_places=2, default=345345, max_digits=15, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CustomerDetails',
        ),
    ]
