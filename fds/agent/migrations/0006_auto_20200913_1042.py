# Generated by Django 3.0.6 on 2020-09-13 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_auto_20200913_1042'),
        ('agent', '0005_auto_20200913_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent_docs',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Delivery_agent'),
        ),
    ]
