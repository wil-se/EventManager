# Generated by Django 3.2.7 on 2021-09-11 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_x_space_gymconfig_width_space'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gymconfig',
            old_name='y_field',
            new_name='height_field',
        ),
        migrations.RenameField(
            model_name='gymconfig',
            old_name='y_space',
            new_name='height_space',
        ),
        migrations.RenameField(
            model_name='gymconfig',
            old_name='x_field',
            new_name='width_field',
        ),
    ]
