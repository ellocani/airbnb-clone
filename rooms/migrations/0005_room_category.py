# Generated by Django 5.1.7 on 2025-03-18 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('rooms', '0004_alter_amenity_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
