# Generated by Django 4.2.8 on 2024-01-02 05:45

from django.db import migrations, models
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(unique=True)),
                ('password', models.CharField()),
                ('created_at', models.DateTimeField(default=django.db.models.functions.datetime.Now())),
                ('updated_at', models.DateTimeField(default=django.db.models.functions.datetime.Now())),
            ],
        ),
    ]
