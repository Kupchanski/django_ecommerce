# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_cart_total'),
        ('orders', '0003_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('shipping_total_price', models.DecimalField(decimal_places=2, max_digits=10, default=5.99)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_address', models.ForeignKey(to='orders.UserAddress', related_name='billing_address')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(to='orders.UserAddress', related_name='shipping_address')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
