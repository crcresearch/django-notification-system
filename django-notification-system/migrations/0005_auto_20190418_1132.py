# Generated by Django 2.1.7 on 2019-04-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20190412_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertarget',
            name='user_target_friendly_name',
            field=models.CharField(max_length=100),
        ),
    ]
