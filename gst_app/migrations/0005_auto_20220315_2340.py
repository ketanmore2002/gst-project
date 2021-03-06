# Generated by Django 3.2.12 on 2022-03-15 18:10

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('gst_app', '0004_auto_20220315_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_id', models.CharField(max_length=300, null=True)),
                ('payment', models.CharField(default='Unpaid', max_length=300, null=True)),
                ('pan_card', models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='pan_card/%Y/%m/%D/')),
                ('proof_of_address', models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='proof_of_address/%Y/%m/%D/')),
                ('photograph', models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='photograph/%Y/%m/%D/')),
                ('aadhar_card', models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='aadhar_card/%Y/%m/%D/')),
                ('order_status', models.CharField(default='Order Recieved', max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='documents_id',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
