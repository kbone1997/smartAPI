from django.shortcuts import render
from rest_framework import viewsets
from smartAPI.models import game
from smartAPI.serializers import gameSerializers


# Create your views here.
class gameview(viewsets.ModelViewSet):
    queryset = game.objects.all()
    serializer_class = gameSerializers
