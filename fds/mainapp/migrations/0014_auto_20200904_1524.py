# Generated by Django 3.0.6 on 2020-09-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20200904_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(default='Snagar', max_length=100),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='state',
            field=models.CharField(default='Snagar', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent_rating',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Delivery_agent'),
        ),
        migrations.AlterField(
            model_name='agent_rating',
            name='reg_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Reg_user'),
        ),
        migrations.AlterField(
            model_name='ambience',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='discount_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Discount'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='dish_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Dish'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='reg_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Reg_user'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='cuisine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Cuisine'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='food_rating',
            name='dish_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Dish'),
        ),
        migrations.AlterField(
            model_name='food_rating',
            name='reg_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Reg_user'),
        ),
        migrations.AlterField(
            model_name='order',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Delivery_agent'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reg_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Reg_user'),
        ),
    ]
