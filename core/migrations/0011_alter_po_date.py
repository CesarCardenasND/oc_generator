# Generated by Django 4.0.2 on 2022-02-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_po_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='po',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
