# Generated by Django 4.2.6 on 2023-11-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('identifier', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
