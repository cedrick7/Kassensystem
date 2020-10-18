# Generated by Django 3.1.2 on 2020-10-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200905_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.DecimalField(blank=True, decimal_places=2, max_digits=15, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='customer',
            name='birthday',
            field=models.DateField(default=None, max_length=45),
        ),
        migrations.AddField(
            model_name='customer',
            name='details',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.customerdetails'),
        ),
    ]