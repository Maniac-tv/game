# Generated by Django 3.2.2 on 2021-10-30 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0010_teams_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='invisible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teams',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]