from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.

rooms = [
    {'id': 1, 'name' : 'Lets learn Python'},
    {'id': 2, 'name' : 'Design and Code'},
    {'id': 3, 'name' : 'Frontend Developers'},
    {'id': 4, 'name' : 'Backend Developers'}
]

def home(request):
    rooms = Room.objects.all() 
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)#Passing in a dictionary and specifying the value names

def room(request, pk): #pk-primary key
    #In order to get the pk value, later on we'll use this primary key to query the database but for now we'll use the variable rooms to create some logic
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)

def createRoom(request): 
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
 
    context = {'form': form} 
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id= pk)
    form = RoomForm(instance=room)
    #We passed in the instance, so, this form will be prefilled with this room value
    #When the values don't match then this is not going to work

    context = {'form': form}
    return render(request, 'base/room_form.html', context)