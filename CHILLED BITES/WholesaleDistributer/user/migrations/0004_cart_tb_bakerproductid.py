# Generated by Django 4.1.3 on 2022-12-30 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homebaker', '0009_alter_productbaker_tb_adminprice'),
        ('user', '0003_userregistration_tb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_tb',
            name='BakerProductId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homebaker.productbaker_tb'),
        ),
    ]
