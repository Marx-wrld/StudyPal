from django.db import models
from django.contrib.auth.models import AbstractUser
#we are no longer using the default user model that django gives us

# Create your models here.
class User(AbstractUser):
    pass


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True) 
    #can't be blank, we can now submit a blank description
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    #The newest updated item will be first. the dash actually inverts it so that the newest s first

    #string representation of this room
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #When a room is deleted the messages will also be deleted from also the database
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] #ordering new messages by the newest

    def __str__(self):
        return self.body[0:50] #we only want the 1st 50 characters