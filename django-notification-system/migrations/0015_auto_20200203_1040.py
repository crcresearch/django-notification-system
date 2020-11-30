# Generated by Django 2.2.8 on 2020-02-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0014_auto_20200131_1551'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usertarget',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='usertarget',
            constraint=models.UniqueConstraint(fields=('user', 'target', 'user_target_id'), name='user target ids cannot be repeated'),
        ),
        migrations.AddConstraint(
            model_name='usertarget',
            constraint=models.UniqueConstraint(condition=models.Q(active=True), fields=('user', 'target', 'user_target_friendly_name'), name='Only one active user target per friendly name'),
        ),
    ]
