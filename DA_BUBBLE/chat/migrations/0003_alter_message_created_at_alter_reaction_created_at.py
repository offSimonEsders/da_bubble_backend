# Generated by Django 5.0.3 on 2024-03-19 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_created_at_alter_reaction_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 3, 19, 15, 18, 44, 390532)),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 3, 19, 15, 18, 44, 390735)),
        ),
    ]
