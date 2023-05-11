from django.db import models

# Create your models here.
class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True) 
    #can't be blank, we can now submit a blank description
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #string representation of this room
    def __str__(self):
        return self.name
