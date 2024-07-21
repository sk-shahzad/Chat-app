from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Message

# Create your views here.

def home(request):
    # form = MessageForm()
    # return render(request, 'home.html', {'form': form})
     chats = Message.objects.all()
     if request.method == 'POST':
        content = request.POST['content']
        chat = Message(sender=request.user, content=content)
        chat.save()


     context = {'chats': chats}
     return render(request, 'home.html', context)

# def send(request):

