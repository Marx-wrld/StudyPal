from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

#Creating Views that is the function based views
def home(request): #request object, the request object is the http, this is going to tell us what kind of request method is sent, what kind of data is being passed in and what is the user sending to the backend
    return HttpResponse(('Home page'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
