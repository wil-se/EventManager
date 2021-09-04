# Generated by Django 3.2.7 on 2021-09-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_match_tournament_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='category',
            field=models.CharField(blank=True, choices=[('Seconda divisione maschile', 'Seconda divisione maschile'), ('Seconda divisione femminile', 'Seconda divisione femminile'), ('MINIVOLLEY', 'MINIVOLLEY')], max_length=256, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament_day',
            field=models.IntegerField(default=0),
        ),
    ]
