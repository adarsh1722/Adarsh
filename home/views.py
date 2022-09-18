from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.


def home(request):
    # return HttpResponse("This is my homepage(/)")
    # context = {'name': 'swati'}
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("This is about myself")
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse("This is about project")
    return render(request, 'projects.html')


def contact(request):
    # return HttpResponse("This is contact me")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
    return render(request, 'contact.html')
