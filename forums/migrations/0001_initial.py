# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
