# Generated by Django 3.2.2 on 2021-10-30 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='game_id',
            field=models.TextField(db_index=True, default=1, max_length=20),
            preserve_default=False,
        ),
    ]