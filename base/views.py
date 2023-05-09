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

def room(request, pk):
    return render(request, 'base/room.html')