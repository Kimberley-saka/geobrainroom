# Generated by Django 4.2.6 on 2023-10-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_course_id_lessons_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
