# Generated by Django 4.2.2 on 2023-06-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0029_section_free_count_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_free_lessons',
            field=models.CharField(default='Free lessons: ', max_length=100),
        ),
    ]
