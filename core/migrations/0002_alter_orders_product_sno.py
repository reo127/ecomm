# Generated by Django 3.2.4 on 2021-08-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product_sno',
            field=models.IntegerField(default=0),
        ),
    ]
