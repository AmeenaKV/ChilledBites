# Generated by Django 4.1.3 on 2022-12-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebaker', '0008_alter_productbaker_tb_adminprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbaker_tb',
            name='AdminPrice',
            field=models.CharField(default='', max_length=20),
        ),
    ]