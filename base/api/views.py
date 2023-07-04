from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room

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
    return Response(rooms)
#Response cannot return back python objects, it ws able to serialize it in routes because it was a dictionary