# Generated by Django 3.2.4 on 2021-06-25 06:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0008_alter_userdetails_pphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userdetails')),
            ],
        ),
    ]
