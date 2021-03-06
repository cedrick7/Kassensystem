# Generated by Django 3.1.2 on 2020-10-30 17:05

import colorfield.fields
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'verbose_name_plural': 'categorien',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, null=True)),
                ('factor', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('amount', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(Decimal('-0.01'))])),
                ('begin', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'discounte',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, null=True)),
                ('taxrate', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(Decimal('-0.01'))])),
            ],
            options={
                'verbose_name_plural': 'taxsätze',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('costs', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('-0.01'))])),
                ('weight', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('-0.01'))])),
                ('stock', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(Decimal('-0.01'))])),
                ('brand', models.CharField(blank=True, max_length=45)),
                ('path', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('type', models.CharField(choices=[('DI', 'Dienstleistung'), ('PR', 'Produkt')], default='PR', max_length=2)),
                ('attributes', models.ManyToManyField(blank=True, to='product.Attribute')),
                ('category', models.ManyToManyField(blank=True, to='product.Category')),
                ('discount', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.discount')),
                ('tax', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.tax')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['type'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='discount',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.discount'),
        ),
    ]
