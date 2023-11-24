# Generated by Django 4.2.6 on 2023-11-22 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pitches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('teacher_weight_score', models.DecimalField(decimal_places=2, default=1, max_digits=3)),
                ('student_weight_score', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('mode', models.CharField(choices=[('asynchronous', 'Asynchronous'), ('synchronous', 'Synchronous')], default='synchronous', max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('course', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('presentors', models.ManyToManyField(to='pitches.pitch')),
            ],
        ),
    ]
