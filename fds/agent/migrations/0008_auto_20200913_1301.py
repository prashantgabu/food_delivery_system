# Generated by Django 3.0.6 on 2020-09-13 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0043_auto_20200913_1301'),
        ('agent', '0007_auto_20200913_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent_docs',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Delivery_agent'),
        ),
    ]
