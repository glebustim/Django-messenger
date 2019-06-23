from typing import Dict
from django.shortcuts import render, HttpResponse
from social.models import Room
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import json
from users_online.views import test_1


# Create your views here.

def main(request):
    context = {}
    context['users'] = User.objects.all().count()
    context['users_online'] = test_1()
    return render(request, 'social/main.html', context)


def manage_access_users(request):
    if not request.user.is_staff:
        return HttpResponse('access x')
    print('manage_users')
    if request.method == 'GET':
        context = {}
        context['users'] = User.objects.all()
        context['rooms'] = Room.objects.all()
        # context['ual'] = UserAccessLevels.objects.all()

        data = {}
        for user in context['users']:
            data[user.username] = {}
            for room in context['rooms']:
                try:
                    access_level = RoomAccess.objects.get(user=user, room=room).access
                except RoomAccess.DoesNotExist:
                    access_level = 0
                data[user.username][room.name] = access_level
        context['data'] = data
        print(context)
        return render(request, 'social/manage_access_user.html', context)

    else:
        s = request.POST
        data = json.loads(s['data'])
        for username in data:
            user = User.objects.get(username=username)
            for roomname in data[username]:
                room = Room.objects.get(name=roomname)
                ual, created = RoomAccess.objects.get_or_create(user=user, room=room)
                ual.access = int(data[username][roomname])
                ual.save()
        return HttpResponse('ok')


@login_required
def rooms(request):
    context = {}
    context['form'] = newRoomForm()
    all_rooms = Room.objects.all()
    all_friends = request.user.profile.friends.all()
    print(all_friends)
    context['friends_rooms'] = all_rooms.filter(creator__profile__in = request.user.profile.friends.all())
    context['other_rooms'] = all_rooms.exclude(creator__profile__in = request.user.profile.friends.all())
    print('post', request.POST)
    if request.method == 'POST':
        print('post')
        form = newRoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            print('save!')
            context['room'] = room
            return render(request, 'social/one_room.html', context)
        else:
            context['form'] = form
    return render(request, 'social/rooms.html', context)

def users(request):
    context = {}
    context['users'] = User.objects.all()
    return render(request, 'social/users.html', context)


def action(request):
    action = request.POST['action']
    id = request.POST['id']
    print('action=',action)
    new_friend = User.objects.get(id=id)
    request.user.profile.friends.add(new_friend.profile)
    return HttpResponse('ok')

@login_required
def user(request, id):
    context = {}
    context['usern'] = Profile.objects.get(id=id)
    return render(request, 'social/user.html', context)


@login_required
def room(request, id):
    context = {}
    context['form'] = newMessageForm()
    if request.method == 'POST':
        form = newMessageForm(request.POST)
        if form.is_valid():
            context['message'] = form.save()
            return render(request, 'social/one_msg.html', context)

    context['room'] = Room.objects.get(id=id)
    return render(request, 'social/room.html', context)
