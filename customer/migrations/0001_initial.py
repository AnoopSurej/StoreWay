# Generated by Django 3.2 on 2021-06-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopkeeper_email', models.EmailField(max_length=254)),
                ('customerFirstName', models.CharField(max_length=30)),
                ('customerLastName', models.CharField(max_length=30)),
                ('customerEmail', models.EmailField(max_length=254)),
                ('customerPhone', models.CharField(max_length=10)),
                ('queueEnterTime', models.DateTimeField(auto_now=True)),
                ('queueTimeSlot', models.CharField(default='Default', max_length=10)),
            ],
        ),
    ]