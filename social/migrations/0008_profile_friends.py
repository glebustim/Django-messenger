# Generated by Django 2.2.1 on 2019-06-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20190614_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='_profile_friends_+', to='social.Profile'),
        ),
    ]
