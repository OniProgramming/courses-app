# Generated by Django 4.2 on 2023-06-12 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0019_lessons_lesson_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='lesson_description',
            field=models.TextField(),
        ),
    ]
