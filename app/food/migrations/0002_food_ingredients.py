# Generated by Django 2.1.3 on 2021-12-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0001_initial'),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(to='ingredient.Ingredient'),
        ),
    ]