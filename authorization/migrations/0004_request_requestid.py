# Generated by Django 3.1.1 on 2020-10-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_auto_20201010_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='requestid',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
