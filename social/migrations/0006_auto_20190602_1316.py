# Generated by Django 2.2.1 on 2019-06-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20190602_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, default='Здесь должна находиться инфрмация о пользователе', null=True),
        ),
    ]
