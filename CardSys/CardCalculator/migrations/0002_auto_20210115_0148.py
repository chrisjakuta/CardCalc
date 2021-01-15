# Generated by Django 3.0.3 on 2021-01-15 01:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CardCalculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIRTELProvider',
            fields=[
                ('airtimeprovider_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CardCalculator.AirTimeProvider')),
                ('total_balance', models.DecimalField(decimal_places=2, help_text='The total balance for all card packs purchased. ', max_digits=9)),
                ('price_per_pack', models.DecimalField(decimal_places=2, help_text='The price for every pack of airtime cards, eg ->  550 cards price * number of cards per pack ', max_digits=9)),
            ],
            options={
                'verbose_name': 'MTN Card',
                'verbose_name_plural': 'MTN Cards',
            },
            bases=('CardCalculator.airtimeprovider',),
        ),
        migrations.CreateModel(
            name='GLOProvider',
            fields=[
                ('airtimeprovider_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CardCalculator.AirTimeProvider')),
                ('total_balance', models.DecimalField(decimal_places=2, help_text='The total balance for all card packs purchased. ', max_digits=9)),
                ('price_per_pack', models.DecimalField(decimal_places=2, help_text='The price for every pack of airtime cards, eg ->  550 cards price * number of cards per pack ', max_digits=9)),
            ],
            options={
                'verbose_name': 'MTN Card',
                'verbose_name_plural': 'MTN Cards',
            },
            bases=('CardCalculator.airtimeprovider',),
        ),
        migrations.AlterModelOptions(
            name='mtnprovider',
            options={'verbose_name': 'MTN Card', 'verbose_name_plural': 'MTN Cards'},
        ),
        migrations.AlterField(
            model_name='airtimeprovider',
            name='card_pack_quantity',
            field=models.PositiveIntegerField(default=0, help_text='How many card packs are available?'),
        ),
        migrations.CreateModel(
            name='AirtimeCardPurchase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_balance', models.DecimalField(decimal_places=2, help_text='The total balance for all card packs purchased. ', max_digits=9)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased', to='CardCalculator.AirTimeProvider')),
            ],
            options={
                'verbose_name': 'Air Time Card Purchase',
                'verbose_name_plural': 'Air Time Card Purchases',
            },
        ),
    ]
