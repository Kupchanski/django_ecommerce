# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20151030_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(max_digits=50, default=0.0, decimal_places=2),
        ),
    ]
