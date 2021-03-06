# Generated by Django 3.2 on 2021-06-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0005_auto_20210530_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopRegistry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopkeeper_email', models.EmailField(max_length=254)),
                ('customerFirstName', models.CharField(max_length=20)),
                ('customerLastName', models.CharField(max_length=20)),
                ('customerPhone', models.CharField(max_length=10)),
                ('queueTimeSlot', models.TimeField()),
                ('shopEnterTime', models.TimeField(auto_now=True)),
            ],
        ),
    ]
