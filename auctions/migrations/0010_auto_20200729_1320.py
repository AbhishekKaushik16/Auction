# Generated by Django 3.0.6 on 2020-07-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200729_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bids',
            options={'verbose_name_plural': 'Bids'},
        ),
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]