# Generated by Django 3.2 on 2021-06-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210605_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=30)),
                ('customerEmail', models.EmailField(max_length=254)),
                ('is_read', models.BooleanField(default=False)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
