# Generated by Django 5.0.6 on 2024-06-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_reservation_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(),
        ),
    ]