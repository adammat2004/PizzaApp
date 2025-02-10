# Generated by Django 5.1.5 on 2025-02-03 13:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaOrder', '0009_alter_pizzaorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaorder',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
