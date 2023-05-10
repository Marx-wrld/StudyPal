from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name' : 'Lets learn Python'},
    {'id': 2, 'name' : 'Design and Code'},
    {'id': 3, 'name' : 'Frontend Developers'},
    {'id': 4, 'name' : 'Backend Developers'}
]

def home(request): 
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)#Passing in a dictionary and specifying the value names

def room(request, pk): #pk-primary key
    #In order to get the pk value, later on we'll use this primary key to query the database but for now we'll use the variable rooms to create some logic
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)