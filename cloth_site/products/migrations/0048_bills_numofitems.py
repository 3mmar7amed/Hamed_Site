# Generated by Django 3.2.6 on 2021-08-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0047_remove_profit_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='numOfItems',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]
