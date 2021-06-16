from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        option = request.POST.get("option")
        desc = request.POST.get("desc")
        contacts = Contacts(name=name, email=email, phone=phone, option=option, desc=desc, date=datetime.today())
        contacts.save()
        messages.success(request, "We recieved your quey and we'll reach out to you soon!")
    return render(request,"contacts.html")

def Anime(request):
    return render(request,"Anime.html")

def Genres(request):
    return render(request,"Genres.html")

def References(request):
    return render(request,"References.html")

def DeliveryOptions(request):
    return render(request,"DeliveryOptions.html")