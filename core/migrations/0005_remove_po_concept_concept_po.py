# Generated by Django 4.0.2 on 2022-02-24 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_po_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='po',
            name='concept',
        ),
        migrations.AddField(
            model_name='concept',
            name='PO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.po'),
        ),
    ]
