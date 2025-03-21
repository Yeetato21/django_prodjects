# Generated by Django 4.2.7 on 2025-03-21 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('basevalue', models.IntegerField(default=1)),
                ('desc', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1)),
                ('color', models.CharField(default='Grey', max_length=16)),
                ('holo', models.CharField(default='None', max_length=32)),
                ('num', models.IntegerField(default=0)),
                ('cointype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin.cointype')),
                ('owners', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
