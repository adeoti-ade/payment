# Generated by Django 2.2.18 on 2021-04-24 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_token_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='otp',
            new_name='token',
        ),
    ]
