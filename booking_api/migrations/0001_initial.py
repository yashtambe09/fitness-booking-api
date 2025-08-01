# Generated by Django 5.2.2 on 2025-06-08 18:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Yoga', 'Yoga'), ('Zumba', 'Zumba'), ('HIIT', 'HIIT')], max_length=50)),
                ('datetime', models.DateTimeField()),
                ('instructor', models.CharField(max_length=100)),
                ('total_slots', models.PositiveIntegerField()),
                ('available_slots', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
                ('booked_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('fitness_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_api.fitnessclass')),
            ],
        ),
    ]
