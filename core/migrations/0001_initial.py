# Generated by Django 3.2.4 on 2021-08-17 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sno', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60)),
                ('landMark', models.CharField(max_length=30)),
                ('opitonlAddress', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=10)),
                ('payment', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default='0')),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('images', models.ImageField(default='', upload_to='core/images')),
            ],
        ),
    ]
