# Generated by Django 3.1.2 on 2020-10-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20201017_1630'),
        ('cashbox', '0004_auto_20200905_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='paymenttool',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='reversalbill',
            name='pdf',
        ),
        migrations.AddField(
            model_name='bill',
            name='path',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='administration.path'),
        ),
        migrations.AddField(
            model_name='paymenttool',
            name='path',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='administration.path'),
        ),
        migrations.AddField(
            model_name='reversalbill',
            name='path',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='administration.path'),
        ),
    ]