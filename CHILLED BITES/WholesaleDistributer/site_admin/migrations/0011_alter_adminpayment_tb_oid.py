# Generated by Django 4.1.3 on 2023-03-18 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_orderitem_tb_oid'),
        ('site_admin', '0010_adminpayment_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpayment_tb',
            name='Oid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order_tb'),
        ),
    ]
