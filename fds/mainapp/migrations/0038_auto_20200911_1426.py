# Generated by Django 3.0.6 on 2020-09-11 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_auto_20200909_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='reg_user',
            name='role',
        ),
        migrations.RemoveField(
            model_name='reg_user',
            name='state',
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
            name='photos',
            field=models.ImageField(default='None', upload_to='ambience_photos'),
        ),
        migrations.AlterField(
            model_name='ambience',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='ambience',
            name='status',
            field=models.CharField(default='not verified', max_length=100),
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
            model_name='cuisine',
            name='cuisine_photo',
            field=models.ImageField(default='None', upload_to='cuisine_photos'),
        ),
        migrations.AlterField(
            model_name='delivery_agent',
            name='status',
            field=models.CharField(default='not verified', max_length=100),
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
            name='dish_photo',
            field=models.ImageField(default='None', upload_to='dish_photos'),
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
            model_name='reg_user',
            name='profile_pic',
            field=models.ImageField(default='None', upload_to='profile_picture'),
        ),
        migrations.AlterField(
            model_name='reg_user',
            name='status',
            field=models.CharField(default='not verified', max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Order'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(default='None', upload_to='res_logo'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='status',
            field=models.CharField(default='not verified', max_length=100),
        ),
        migrations.AlterField(
            model_name='verification',
            name='pan_card',
            field=models.ImageField(default='None', upload_to='verification_photos'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='res_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='shop_fssai_license',
            field=models.ImageField(default='None', upload_to='verification_photos'),
        ),
    ]
