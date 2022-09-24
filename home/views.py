from token import NAME
from tokenize import Name
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse('This is my new home app(/)')
    return render(request, 'home.html')

def about(request):
    #return HttpResponse('This is my new about app(/about)')
    return render(request, 'about.html')

def projects(request):
   # return HttpResponse('This is my new projects app(/projects)')
   return render(request, 'projects.html')


def Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        contact= Contact(name=name, email=email, phone=phone, desc=desc )
        contact.save()
    #return HttpResponse('This is my new contact app(/contact)')
    return render(request, 'contact.html')
   