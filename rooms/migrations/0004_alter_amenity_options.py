# Generated by Django 5.1.7 on 2025-03-18 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_name_alter_amenity_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
    ]
