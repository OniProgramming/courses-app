# Generated by Django 4.2 on 2023-06-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_alter_course_type_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subtitle',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
