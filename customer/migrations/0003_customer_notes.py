# Generated by Django 3.0.8 on 2020-11-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20201104_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]