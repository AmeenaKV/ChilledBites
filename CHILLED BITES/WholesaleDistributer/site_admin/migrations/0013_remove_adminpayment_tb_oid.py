# Generated by Django 4.1.3 on 2023-03-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0012_alter_adminpayment_tb_oid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminpayment_tb',
            name='Oid',
        ),
    ]