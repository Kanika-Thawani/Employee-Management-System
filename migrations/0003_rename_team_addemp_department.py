# Generated by Django 3.2.4 on 2021-07-18 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_addemp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addemp',
            old_name='team',
            new_name='department',
        ),
    ]
