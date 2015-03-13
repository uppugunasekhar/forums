# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0004_auto_20150128_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='sub',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='uid',
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.ForeignKey(default=0, to='forums.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
