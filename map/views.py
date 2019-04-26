from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from map.models import Room as RoomModel, Location
import uuid
import json


class Create(View):
	template_name='create.html'

	def get(self,request,*args,**kwargs):
		uid = str(uuid.uuid1())
		room = RoomModel(uid=uid)
		room.save()
		return HttpResponseRedirect('/map/room/' + uid)


class Room(View):
	template_name='room.html'

	def get(self,request,*args,**kwargs):
		rid = RoomModel.objects.filter(uid=kwargs['uid'])[0].id
		return render(request, 'room.html', {'room': rid})


class UpdateLocation(View):

	def get(self, request, *args, **kwargs):
		user = request.session["user"]
		lat = kwargs["lat"]
		lng = kwargs["lng"]
		room_id = kwargs["room"]

		room = RoomModel.objects.filter(id=room_id)[0]
		loc = Location.objects.filter(room=room)
		# print(loc.values())

		if (len(loc) <= 0):
			loc = Location(lat=lat, lng=lng, user=user, room=room)
		else:
			loc = loc[0]
			loc.lat = lat
			loc.lng = lng
		loc.save()
		
		return HttpResponse("success")


class GetLocations(View):

	def get(self,request,*args,**kwargs):
		if "user" not in request.session:
			user = str(uuid.uuid1())
			request.session["user"] = user
			room = RoomModel.objects.filter(id=kwargs["room"])[0]
			loc = Location(lat=kwargs["lat"], lng=kwargs["lng"], user=user, room=room)
			loc.save()
		rid = kwargs["room"]
		locs = Location.objects.filter(room=rid)
		data = json.dumps([{'lat':loc.lat,'lng':loc.lng} for loc in locs])
		return HttpResponse(data)