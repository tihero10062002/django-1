# Generated by Django 4.2.3 on 2023-08-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_phone_number', models.CharField(max_length=255)),
            ],
        ),
    ]