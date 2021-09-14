# Generated by Django 3.2.7 on 2021-09-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(default='/logo.png', upload_to='teams/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='/global_assets/images/placeholders/placeholder.jpg', upload_to='teams/'),
        ),
    ]