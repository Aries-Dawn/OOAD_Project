# Generated by Django 2.2 on 2020-12-25 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
        ('user', '0002_auto_20201225_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='game',
            field=models.ManyToManyField(blank=True, to='game.Game'),
        ),
    ]