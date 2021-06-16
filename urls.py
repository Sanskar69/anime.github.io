from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("services",views.services,name="services"),
    path("contacts",views.contacts,name="contacts"),
    path("Genres",views.Genres,name="Genres"),
    path("Anime",views.Anime,name="Anime"),
    path("References",views.References,name="References"),
    path("DeliveryOptions",views.DeliveryOptions,name="DeliveryOptions"),



]