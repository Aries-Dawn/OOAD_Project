# Generated by Django 2.2 on 2020-12-19 09:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
            ],
        ),
    ]
