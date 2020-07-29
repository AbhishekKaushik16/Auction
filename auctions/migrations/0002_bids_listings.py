# Generated by Django 3.0.6 on 2020-07-19 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('item_price', models.IntegerField()),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.Listings')),
            ],
        ),
    ]
