# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_uid',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
