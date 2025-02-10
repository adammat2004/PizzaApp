# Generated by Django 5.1.5 on 2025-02-03 13:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaOrder', '0012_pizzaorder_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaorder',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
