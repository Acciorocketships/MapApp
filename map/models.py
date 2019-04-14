from django.db import models

class Room(models.Model):
	uid = models.CharField(max_length=36)
	
class Location(models.Model):
	lat = models.CharField(max_length=15)
	lng = models.CharField(max_length=15)
	user = models.CharField(max_length=36)
	room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)

