# Generated by Django 4.2.2 on 2023-07-15 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='location_type',
        ),
    ]