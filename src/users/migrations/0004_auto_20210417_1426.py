# Generated by Django 2.2.18 on 2021-04-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210417_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='token',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='token',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='expires_at',
            new_name='expires',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='token',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]