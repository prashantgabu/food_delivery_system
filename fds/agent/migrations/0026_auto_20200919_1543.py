# Generated by Django 3.0.6 on 2020-09-19 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0061_auto_20200919_1543'),
        ('agent', '0025_auto_20200919_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent_docs',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Delivery_agent'),
        ),
    ]
