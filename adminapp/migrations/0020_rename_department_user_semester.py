# Generated by Django 4.2.10 on 2024-12-11 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_remove_user_fname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='department',
            new_name='semester',
        ),
    ]