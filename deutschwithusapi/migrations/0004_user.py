# Generated by Django 5.0.4 on 2024-07-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deutschwithusapi', '0003_remove_resume_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
