# Generated by Django 3.2.2 on 2021-07-21 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0005_auto_20210712_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.TextField(db_index=True, max_length=20)),
                ('game_name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=5000)),
                ('inventory', models.TextField(max_length=500)),
                ('pointers', models.TextField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
