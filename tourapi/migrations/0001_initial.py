# Generated by Django 5.0.1 on 2024-02-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nid_number', models.CharField(max_length=13)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('package_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
