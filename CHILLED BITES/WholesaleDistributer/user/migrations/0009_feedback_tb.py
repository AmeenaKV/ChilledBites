# Generated by Django 4.1.3 on 2023-02-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_orderitem_tb_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=20)),
            ],
        ),
    ]
