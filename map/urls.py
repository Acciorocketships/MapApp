from django.urls import path
from map.views import *

urlpatterns = [
    path('create', Create.as_view()),
    path('room/<str:uid>', Room.as_view()),
    path('room/location/<str:room>/<str:lat>/<str:lng>', GetLocations.as_view()),
    path('room/location/<str:room>/<str:lat>/<str:lng>', UpdateLocation.as_view()),
    ]