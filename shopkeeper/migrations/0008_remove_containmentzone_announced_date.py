# Generated by Django 3.2 on 2021-06-05 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0007_containmentzone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='containmentzone',
            name='announced_date',
        ),
    ]