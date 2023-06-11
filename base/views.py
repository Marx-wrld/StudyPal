from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

rooms = [
    {'id': 1, 'name' : 'Lets learn Python'},
    {'id': 2, 'name' : 'Design and Code'},
    {'id': 3, 'name' : 'Frontend Developers'},
    {'id': 4, 'name' : 'Backend Developers'}
]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' #q is going to be equal to whatever we passed in the url
    
    rooms = Room.objects.filter(topic__name__icontains = q)#going to the model file and getting the topic, and querying upwards to the parent(__)
    #icontains will make sure that whatever value we have in our topic name atleast contains whats in here(topic)

    topics = Topic.objects.all()

    context = {'rooms':rooms, 'topics': topics}
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
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #This is going to tell our function what room to update
        if form.is_valid():
            form.save()
            return redirect('home')#sends the user back to the home page

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})