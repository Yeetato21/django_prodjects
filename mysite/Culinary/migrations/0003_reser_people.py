# Generated by Django 5.1.5 on 2025-02-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Culinary', '0002_rename_time_reser_t_rename_time_timeslot_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='reser',
            name='people',
            field=models.IntegerField(default=1),
        ),
    ]
