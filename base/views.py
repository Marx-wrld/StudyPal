from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id': 1, 'name' : 'Lets learn Python'},
#     {'id': 2, 'name' : 'Design and Code'},
#     {'id': 3, 'name' : 'Frontend Developers'},
#     {'id': 4, 'name' : 'Backend Developers'}
# ]

def loginPage(request):

    page = 'login'

    #Saving user details after they are already logged in
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username) #checking if this user exists if not we want to throw in an error
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password) #authenticate either throws in an error or throws in a user object that matches these credentials.

        if user is not None:
            login(request, user) 
            return redirect('home')
            #login adds this session into our database and then inside our browser
        else:
            messages.error(request, 'Username OR Password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
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
            messages.error(request, 'An error occurred during registration!')
            
    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' #q is going to be equal to whatever we passed in the url
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
            Q(description__icontains = q) 
        )
    #Dynamic searches
    #going to the model file and getting the topic, and querying upwards to the parent(__)
    #icontains will make sure that whatever value we have in our topic name atleast contains whats in here(topic)

    topics = Topic.objects.all()

    room_count = rooms.count() #You can also use the python len() method

    context = {'rooms':rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)#Passing in a dictionary and specifying the value names

def room(request, pk): #pk-primary key
    #In order to get the pk value, later on we'll use this primary key to query the database but for now we'll use the variable rooms to create some logic
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all() #Give me the set of messages related to this room
    context = {'room': room, 'room_messages': room_messages}

    return render(request, 'base/room.html', context)

#restricting some pages regardless of whether they are logged in or logged out
@login_required(login_url='login')
def createRoom(request): 
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
 
    context = {'form': form} 
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id= pk)
    form = RoomForm(instance=room)
    #We passed in the instance, so, this form will be prefilled with this room value
    #When the values don't match then this is not going to work
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here!') 

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #This is going to tell our function what room to update
        if form.is_valid():
            form.save()
            return redirect('home')#sends the user back to the home page

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!') 

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})