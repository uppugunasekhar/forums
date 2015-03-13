# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_auto_20150206_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.ForeignKey(default=0, to='forums.Subject'),
            preserve_default=True,
        ),
    ]
