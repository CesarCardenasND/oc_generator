# Generated by Django 4.0.2 on 2022-02-23 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='po',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='po',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='po',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]