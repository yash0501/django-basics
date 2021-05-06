from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable": "Hello World"
    }
    return render(request, "index.html", context)
    #return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About Page")

def add_advisor(request):
    return HttpResponse("This is Add Advisor Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        contact = Contact(name=name, email=email, phone=phone, date=datetime.today())
        contact.save()
    return render(request, "contact.html")

def contact1(request, year):
    return HttpResponse(year)