# Generated by Django 4.1.3 on 2023-02-18 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_remove_feedback_tb_bakerid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameonCard', models.CharField(max_length=20)),
                ('CreditCardNumber', models.CharField(max_length=20)),
                ('CVV', models.CharField(max_length=20)),
                ('ExpDate', models.CharField(max_length=20)),
                ('Amount', models.CharField(max_length=20)),
                ('Oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order_tb')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userregistration_tb')),
            ],
        ),
    ]
