# Generated by Django 5.0.6 on 2024-06-22 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_reservation_class_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssetManager',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='id',
        ),
        migrations.AddField(
            model_name='reviews',
            name='facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.facility'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
