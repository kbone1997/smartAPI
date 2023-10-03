from django.contrib import admin
from django.urls import path, include
from smartAPI import views
from rest_framework import routers  # routers allows us to create get and post request

routers = routers.DefaultRouter()
routers.register("games", views.gameview)

urlpatterns = [path("", include(routers.urls))]
