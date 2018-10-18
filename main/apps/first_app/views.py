from __future__ import unicode_literals
from django.shortcuts import render, redirect
from . models import User

def index(request):
    context={
        "users": User.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def new(request): #Generates the form
    return render(request, 'first_app/new.html')

def create(request):
    #Handle form submission; we're redirecting bc to entire new request and function; context is the vessel through which we send the information to the HTML page; if not rendering any data no context is needed; this function simply creates a user
    
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/') #the url that represents the index function

def show(request, user_id):
    
    #User.objects.get(id=user_id) #where clause in SQL
    context={
        "user": User.objects.get(id=user_id) # it got the entire row of information
    }
    return render(request, 'first_app/show.html', context)

def edit(request, user_id):
    context={
        "user":User.objects.get(id=user_id) #"user" is the key
    }
    return render(request, 'first_app/edit.html', context)

def update(request): #it does not have the user_id parameter like above bc it is hidden
    #request.post is the container that contains the data
    user=User.objects.get(id=request.POST['user_id'])# affect the column; get the User and store it as variable user to affect the bottom columns
    user.first_name=request.POST['first_name']# we got the information update from request.POST info from the html page
    user.last_name=request.POST['last_name']
    user.email=request.POST['email']
    user.save()
    return redirect ('/')

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect ('/')

#post is a vessel that which we just send data; session is another vessel to hold data//post is just a way for us to get  data from a form into a function (dictionary)
    

# Create your views here.
 