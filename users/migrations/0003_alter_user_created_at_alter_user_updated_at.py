# Generated by Django 4.2.8 on 2024-01-02 05:55

from django.db import migrations, models
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.db.models.functions.datetime.Now()),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=django.db.models.functions.datetime.Now()),
        ),
    ]
