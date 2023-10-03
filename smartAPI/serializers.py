from rest_framework import serializers
from smartAPI.models import game


class gameSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = game
        fields = ("id", "url", "name", "genre", "price")
