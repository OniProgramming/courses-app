# Generated by Django 4.2 on 2023-06-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('thumbnail_url', models.CharField(max_length=1000)),
                ('vide_url', models.CharField(max_length=1000)),
                ('type_course', models.CharField(choices=[('free', 'free'), ('paid', 'paid')], default='free', max_length=30)),
                ('course_length', models.CharField(max_length=100)),
            ],
        ),
    ]
