# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0025_auto_20150313_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.ForeignKey(default=0, to='forums.Subject'),
            preserve_default=True,
        ),
    ]
