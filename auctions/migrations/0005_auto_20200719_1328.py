# Generated by Django 3.0.6 on 2020-07-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200719_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='person_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='listings',
            name='listed_by',
            field=models.CharField(max_length=64),
        ),
    ]
