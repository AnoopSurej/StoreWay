# Generated by Django 3.2 on 2021-05-30 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shops',
            old_name='q_solt_capacity',
            new_name='q_slot_capacity',
        ),
    ]