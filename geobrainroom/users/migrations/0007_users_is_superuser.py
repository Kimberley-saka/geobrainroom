# Generated by Django 4.2.6 on 2023-10-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_users_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
