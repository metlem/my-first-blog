# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('yazar', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
                ('yaratilis_tarihi', models.DateTimeField(default=django.utils.timezone.now)),
                ('onaylanmis_yorum', models.BooleanField(default=False)),
                ('post', models.ForeignKey(to='blog.Post', related_name='comments')),
            ],
        ),
    ]
