# Generated by Django 2.1.3 on 2021-12-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
    ]