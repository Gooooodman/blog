# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150514_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u94fe\u63a5\u6807\u9898')),
                ('url', models.CharField(max_length=200, null=True, verbose_name='\u94fe\u63a5\u5730\u5740', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='\u94fe\u63a5\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
            ],
            options={
                'ordering': ['-status'],
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
    ]
