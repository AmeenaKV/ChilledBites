# Generated by Django 4.1.5 on 2023-02-05 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homebaker', '0009_alter_productbaker_tb_adminprice'),
        ('user', '0009_feedback_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_tb',
            name='BakerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homebaker.homebakerregistration_tb'),
        ),
        migrations.AddField(
            model_name='feedback_tb',
            name='UserId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userregistration_tb'),
        ),
    ]
