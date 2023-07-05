from django.contrib import admin
from django.urls import path, include 
#from django.http import HttpResponse

"""Creating Views that is the function based views
def home(request): #request object, the request object is the http, this is going to tell us what kind of request method is sent, what kind of data is being passed in and what is the user sending to the backend
    return HttpResponse(('Home page'))
def room(request):
    return HttpResponse('ROOM')
#This method would be clumsy since we'd have many urls and path on the urls page and that wy django created apps    
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls'))
]

