# Generated by Django 5.0.2 on 2024-06-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_category_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
