# Generated by Django 3.0.8 on 2020-10-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20201020_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='title',
            field=models.CharField(max_length=45, null=True),
        ),
    ]