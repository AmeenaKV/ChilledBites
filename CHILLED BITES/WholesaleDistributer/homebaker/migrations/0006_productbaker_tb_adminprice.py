# Generated by Django 4.1.3 on 2022-12-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebaker', '0005_remove_productbaker_tb_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbaker_tb',
            name='AdminPrice',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
