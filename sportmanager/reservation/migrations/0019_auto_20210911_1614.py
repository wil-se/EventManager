# Generated by Django 3.2.7 on 2021-09-11 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0018_alter_seat_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seatgymconfig',
            old_name='left',
            new_name='left_field',
        ),
        migrations.RenameField(
            model_name='seatgymconfig',
            old_name='top',
            new_name='top_field',
        ),
    ]