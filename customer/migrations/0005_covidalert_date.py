# Generated by Django 3.2 on 2021-06-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_covidalert'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidalert',
            name='date',
            field=models.DateTimeField(default='2021-06-06 00:00'),
            preserve_default=False,
        ),
    ]
