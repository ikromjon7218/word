# Generated by Django 4.2 on 2023-05-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_amount_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount',
            name='lamp',
            field=models.SmallIntegerField(default=3),
        ),
    ]
