# Generated by Django 5.1.3 on 2024-12-03 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_alter_staff_fac_id_alter_stud_stud_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]