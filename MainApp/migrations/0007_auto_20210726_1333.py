# Generated by Django 3.2.2 on 2021-07-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='invisible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='invisible',
            field=models.BooleanField(default=False),
        ),
    ]
