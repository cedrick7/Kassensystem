# Generated by Django 3.0.8 on 2020-10-22 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_auto_20201018_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='path',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Path'),
        ),
    ]
