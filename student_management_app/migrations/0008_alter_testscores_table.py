# Generated by Django 4.2 on 2023-04-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student_management_app", "0007_testscores"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="testscores",
            table="test_scores",
        ),
    ]