# Generated by Django 3.0.8 on 2020-10-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20201021_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='path',
            field=models.FileField(blank=True, default=None, null=True, upload_to='uploads/'),
        ),
    ]
