# Generated by Django 4.2 on 2023-06-09 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='vide_url',
        ),
    ]
