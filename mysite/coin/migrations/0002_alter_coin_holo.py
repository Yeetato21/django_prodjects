# Generated by Django 4.2.7 on 2025-03-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='holo',
            field=models.CharField(default='', max_length=32),
        ),
    ]
