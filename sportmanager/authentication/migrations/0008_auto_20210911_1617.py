# Generated by Django 3.2.7 on 2021-09-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_rename_user_gymconfig_gym'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymconfig',
            name='left_field',
            field=models.IntegerField(default=69),
        ),
        migrations.AddField(
            model_name='gymconfig',
            name='top_field',
            field=models.IntegerField(default=69),
        ),
    ]