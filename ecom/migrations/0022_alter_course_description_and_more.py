# Generated by Django 4.2.2 on 2023-06-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0021_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lesson_description',
            field=models.TextField(),
        ),
    ]
