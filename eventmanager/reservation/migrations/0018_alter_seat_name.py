# Generated by Django 3.2.7 on 2021-09-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0017_auto_20210911_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]