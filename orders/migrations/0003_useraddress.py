# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20151105_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=120, choices=[('billing', 'billing'), ('shipping', 'shipping')])),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
