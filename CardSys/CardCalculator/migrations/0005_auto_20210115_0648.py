# Generated by Django 3.0.3 on 2021-01-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CardCalculator', '0004_auto_20210115_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airtelprovider',
            name='price_per_pack',
        ),
        migrations.RemoveField(
            model_name='gloprovider',
            name='price_per_pack',
        ),
        migrations.RemoveField(
            model_name='mtnprovider',
            name='price_per_pack',
        ),
    ]
