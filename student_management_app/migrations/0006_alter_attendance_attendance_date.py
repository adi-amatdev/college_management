# Generated by Django 4.1.2 on 2023-04-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_sessionyearmodel_remove_students_session_end_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
