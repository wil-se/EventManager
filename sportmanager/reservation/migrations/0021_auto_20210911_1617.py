# Generated by Django 3.2.7 on 2021-09-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0020_auto_20210911_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatgymconfig',
            name='left',
            field=models.IntegerField(default=69),
        ),
        migrations.AddField(
            model_name='seatgymconfig',
            name='top',
            field=models.IntegerField(default=69),
        ),
    ]