# Generated by Django 4.1.5 on 2023-04-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0015_refundpayment_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_tb',
            name='Name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='admin_tb',
            name='Phone_No',
            field=models.CharField(default='', max_length=20),
        ),
    ]
