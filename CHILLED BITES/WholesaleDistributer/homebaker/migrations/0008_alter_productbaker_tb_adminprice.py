# Generated by Django 4.1.3 on 2022-12-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebaker', '0007_alter_productbaker_tb_adminprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbaker_tb',
            name='AdminPrice',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
