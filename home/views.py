from django.shortcuts import render
from django.http import HttpResponse
from .models import ChatRoom
from .models import Message
# Create your views here.

def home(request):
    room = ChatRoom.objects.all()
    return render(request, 'home.html', {'room': room})
