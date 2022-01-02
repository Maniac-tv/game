# Generated by Django 3.2.2 on 2021-11-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0014_teams_game_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='game_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(db_index=True, max_length=50)),
                ('user_id', models.TextField(db_index=True, max_length=75)),
                ('team_id', models.TextField(db_index=True, max_length=25)),
                ('user_ip', models.TextField(db_index=True, max_length=25)),
                ('user_active', models.BooleanField(default=True)),
            ],
        ),
    ]
