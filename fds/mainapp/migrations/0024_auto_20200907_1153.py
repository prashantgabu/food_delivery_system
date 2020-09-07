# Generated by Django 3.0.6 on 2020-09-07 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20200907_1121'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='verification',
            name='gst_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='pan_card',
            field=models.ImageField(upload_to='verification_photos'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='res_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='shop_fssai_license',
            field=models.ImageField(upload_to='verification_photos'),
        ),
    ]