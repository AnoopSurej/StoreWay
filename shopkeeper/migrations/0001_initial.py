# Generated by Django 3.2 on 2021-05-30 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=40)),
                ('shop_type', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=25)),
                ('localbody', models.CharField(max_length=25)),
                ('wardnum', models.IntegerField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('q_slot_time', models.IntegerField()),
                ('q_solt_capacity', models.IntegerField()),
                ('description', models.TextField()),
                ('owner_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
