from typing import Dict
from django.shortcuts import render, HttpResponse
from social.models import Room
from .models import *
from django.contrib.auth.decorators import login_required
import json

def test_1():
    return 12334