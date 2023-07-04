from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request): #view to show us all the routes in our api
    routes = [ 
        'GET /api',
        'GET /api/rooms', #Allows user to get all the rooms from our route
        'GET /api/rooms/:id' #Allows user to get a single room from our route
    ]
    return Response(routes) #[safe=False]safe is going to allow this list to be turned into a JSON list data

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) #many means that their are multiple objects that we are going to serializers
    return Response(serializer.data)
#Response cannot return back python objects, it ws able to serialize it in routes because it was a dictionary

@api_view(['GET']) #view for a single room object
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) 
    return Response(serializer.data)