# Generated by Django 2.2.3 on 2019-07-27 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('purse_app', '0005_auto_20190727_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcards',
            name='grace_period_end',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
    ]
