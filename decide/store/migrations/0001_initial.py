# Generated by Django 2.0 on 2018-12-27 23:58

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.PositiveIntegerField()),
                ('voter_id', models.PositiveIntegerField()),
                ('a', base.models.BigBigField()),
                ('b', base.models.BigBigField()),
                ('voted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
