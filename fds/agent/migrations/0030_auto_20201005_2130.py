# Generated by Django 3.0.6 on 2020-10-05 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0065_auto_20201005_2130'),
        ('agent', '0029_auto_20200930_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent_docs',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Delivery_agent'),
        ),
    ]
