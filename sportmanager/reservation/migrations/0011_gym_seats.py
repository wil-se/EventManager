# Generated by Django 3.2.7 on 2021-09-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_auto_20210904_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='seats',
            field=models.IntegerField(default=0, verbose_name='Posti a sedere'),
        ),
    ]
