from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # print(f"Username:{username},Password:{password}")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
    context = {'page': page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured')

    return render(request, 'login_register.html',{'form':form})

@login_required(login_url='/login')
def home(request):
     user = request.user
     users = User.objects.exclude(id=request.user.id)
     sents = Message.objects.filter(sender=user)
     rec = Message.objects.filter(recipient=user)
     
     if request.method == 'POST':
        recipient_id = request.POST['recipient']
        content = request.POST['content']
        recipient = User.objects.get(id=recipient_id)
        chat = Message(sender=request.user, content=content, recipient=recipient)
        chat.save()


     context = {'sents': sents, 'users': users, 'rec': rec}
     return render(request, 'home.html', context)


