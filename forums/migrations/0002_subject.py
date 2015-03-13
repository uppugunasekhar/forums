# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_title', models.CharField(max_length=50)),
                ('subject_desc', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'published date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
