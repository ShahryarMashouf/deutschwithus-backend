# Generated by Django 5.0.4 on 2024-07-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deutschwithusapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='counselling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
