# Generated by Django 3.0.6 on 2020-09-03 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200903_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('status', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('dish_description', models.TextField(max_length=100)),
                ('dish_photo', models.ImageField(upload_to='dish_photos')),
                ('customization', models.CharField(max_length=100)),
                ('cuisine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cuisine')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.restaurant')),
            ],
            options={
                'db_table': 'dish',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('payment_type', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('order_time', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.delivery_agent')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cart')),
                ('reg_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.reg_user')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='food_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.dish')),
                ('reg_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.reg_user')),
            ],
            options={
                'db_table': 'food_rating',
            },
        ),
        migrations.CreateModel(
            name='discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_value', models.IntegerField()),
                ('discount_description', models.TextField()),
                ('discount_limit', models.IntegerField()),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.restaurant')),
            ],
            options={
                'db_table': 'discount',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='discount_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.discount'),
        ),
        migrations.AddField(
            model_name='cart',
            name='dish_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.dish'),
        ),
        migrations.AddField(
            model_name='cart',
            name='reg_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.reg_user'),
        ),
        migrations.CreateModel(
            name='agent_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.delivery_agent')),
                ('reg_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.reg_user')),
            ],
            options={
                'db_table': 'agent_rating',
            },
        ),
    ]
