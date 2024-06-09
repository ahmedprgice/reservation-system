# Generated by Django 5.0.6 on 2024-05-09 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_manager_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('anemity', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='facility_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Facaulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='faculty_pics')),
                ('facilities', models.ManyToManyField(to='main.facility')),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='reservations',
            field=models.ManyToManyField(to='main.reservation'),
        ),
        migrations.AddField(
            model_name='facility',
            name='reviews',
            field=models.ManyToManyField(to='main.reviews'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.staff'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.staff'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
    ]