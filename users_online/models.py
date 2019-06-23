from django.db import models
from django.contrib.auth.models import User

# coding=utf-8
from django.db import models
from sys import stdout
from django.contrib.auth.models import User
import datetime
# coding=utf-8
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

# class activeUser(models.Model):
#     user = models.ForeignKey(User)
#     datetime_last_active = models.DateTimeField(auto_now_add=True)

