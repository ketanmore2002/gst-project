# Generated by Django 3.2.12 on 2022-03-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gst_app', '0002_alter_orders_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(default='Order Recieved', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment',
            field=models.CharField(default='Unpaid', max_length=300, null=True),
        ),
    ]
