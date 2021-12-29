# Generated by Django 2.1.3 on 2021-12-11 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=30)),
                ('building_number', models.IntegerField()),
                ('type', models.CharField(choices=[('h', 'home'), ('r', 'restaurant')], default=None, max_length=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
