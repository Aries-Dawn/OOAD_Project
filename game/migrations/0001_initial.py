# Generated by Django 2.2.8 on 2020-12-24 21:14

from django.db import migrations, models
import django.db.models.deletion
import read_statistic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.TextField(default='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('lastupdate_time', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(upload_to='game_image/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='developer.Developer')),
            ],
            options={
                'ordering': ['-create_time'],
            },
            bases=(models.Model, read_statistic.models.ReadNum_Expand),
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_num', models.IntegerField(default=1)),
                ('introduction', models.TextField(default='')),
                ('price', models.FloatField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(upload_to='version_image/%Y/%m/%d/')),
                ('file', models.FileField(null=True, upload_to='game_file/%Y/%m/%d/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='game_version', to='game.Game')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.GameType'),
        ),
        migrations.CreateModel(
            name='DLC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.TextField(default='')),
                ('price', models.FloatField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(upload_to='dlc_image/%Y/%m/%d/')),
                ('file', models.FileField(null=True, upload_to='dlc_file/%Y/%m/%d/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dlc_version', to='game.Game')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('GAME', 'GAME'), ('DLC', 'DLC')], default='GAME', max_length=7)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('price', models.FloatField()),
                ('dlc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.DLC')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
            ],
        ),
    ]
