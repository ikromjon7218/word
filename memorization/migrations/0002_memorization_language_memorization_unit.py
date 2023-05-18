# Generated by Django 4.2 on 2023-05-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorization',
            name='language',
            field=models.CharField(default='eng-uzb', max_length=10),
        ),
        migrations.AddField(
            model_name='memorization',
            name='unit',
            field=models.PositiveSmallIntegerField(default=3),
        ),
    ]
