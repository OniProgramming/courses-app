# Generated by Django 4.2 on 2023-06-10 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0013_course_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default='Englsh', max_length=100),
        ),
    ]
