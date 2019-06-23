from django.db import models
from django.contrib.auth.models import User

# coding=utf-8
from django.db import models
from sys import stdout
from django.contrib.auth.models import User
import datetime
# coding=utf-8
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from django.db.models import Count

from django.utils.text import slugify
from django.db.models import F, Max
import re
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True, default="Здесь должна находиться информация о пользователе")
    education = models.CharField(max_length=200, blank=True, null=True, default="Информация отсутствует")
    friends = models.ManyToManyField('self',related_name='friends')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return 'user' + str(self.id)

    def get_access(self,room):
        z = RoomAccess.objects.get(user=self.user,room=room)
        print(z)
        return z

class Room(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' создана ' + self.creator.username

    def get_absolute_url(self):
        return 'room' + str(self.id)

class Message(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок сообщения')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages',verbose_name='Комната')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages',verbose_name='Автор')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True, verbose_name='Текст сообщения')

    def __str__(self):
        return str(self.title) + ' by ' + str(self.author.username)

class RoomAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_rooms')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='access_users')
    access = models.IntegerField(default=settings.ROOM_ACCESS_READ)

# class Subscription(models.Model):
#     sub_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
#     target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
#
#     def __str__(self):
#         return str(self.sub_user.username) + ' подписан на ' + str(self.target.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
