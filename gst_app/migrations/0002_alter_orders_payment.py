# Generated by Django 3.2.12 on 2022-03-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gst_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payment',
            field=models.CharField(default='Order Recieved', max_length=300, null=True),
        ),
    ]
