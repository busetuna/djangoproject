# Generated by Django 5.0.2 on 2024-07-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]