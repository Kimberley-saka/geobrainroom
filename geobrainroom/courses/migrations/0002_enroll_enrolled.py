# Generated by Django 4.2.6 on 2023-10-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='enrolled',
            field=models.BooleanField(null=True),
        ),
    ]
