# Generated by Django 4.2.3 on 2023-08-01 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_application_client_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.course'),
        ),
    ]
