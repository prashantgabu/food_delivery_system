# Generated by Django 3.0.6 on 2020-09-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200903_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_user',
            name='address',
            field=models.TextField(),
        ),
    ]