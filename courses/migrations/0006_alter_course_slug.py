# Generated by Django 4.0.1 on 2022-01-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_slug_alter_course_active_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
