# Generated by Django 3.0.6 on 2020-09-04 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20200904_1505'),
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
        migrations.CreateModel(
            name='Ambience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='ambience_photos')),
                ('status', models.CharField(default='SOME STRING', max_length=100)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Restaurant')),
            ],
            options={
                'db_table': 'ambience',
            },
        ),
    ]