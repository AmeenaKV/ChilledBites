# Generated by Django 4.1.7 on 2023-04-20 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_orderitem_tb_oid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_tb',
            name='PaymentMode',
            field=models.CharField(default='', max_length=20),
        ),
    ]