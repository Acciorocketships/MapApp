# Generated by Django 2.2 on 2019-04-14 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=15)),
                ('lng', models.CharField(max_length=15)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.Room')),
            ],
        ),
    ]