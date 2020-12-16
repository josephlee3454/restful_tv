from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
   
    return render(request, 'index.html')## renders the origiinal html page  

def shows(request): # this function is for my table of items in the db 
    context = {
        "all_shows": NewShow.objects.all()#says i want all items in the model NewShow
    }

    return render(request, 'shows.html', context)

def add_show(request):#this method creates a new model element 

    if request.method == "POST":
        errors = NewShow.objects.validateShow(request.POST)
        if errors:
            for key, value in errors.items():# loops through the dictionary off errors
                messages.error(request, value)# gives a message for every error in dict 
            return redirect("/")# redirect back to home page becuase we want to finish 
        else:
            show = NewShow.objects.create(title = request.POST['title'], network = request.POST['network'], release = request.POST['release'], desc = request.POST['desc'])
            return redirect(f"show_info/{show.id}")#redirect to show info and passes the id throughht the f string 


def show_info(request,show_id):#this method is for my hyper link to show each specific show by its id 
    context = {
        'show': NewShow.objects.get(id=show_id),
        'all_shows': NewShow.objects.all()
    }
    
    return render(request, 'show_info.html', context)

def delete_show(request,show_id):# this method is for my deletion of a element 
    show = NewShow.objects.get(id=show_id)
    show.delete()#delete method this builtin method will delete the objs you put on a varible 
    return redirect('/shows')

def edit_show(request, show_id):## this functions sole purpose is to bring us to a page with our old value already in the fields 
    context = {
    'show': NewShow.objects.get(id=show_id),
    'all_shows': NewShow.objects.all()
        
    }
    return render(request, 'edit.html', context)

def show_update(request, show_id):# this function actually updates by sending a new post request that overwrites the old db info
        if request.method == "POST":
            errors = NewShow.objects.validateShow(request.POST)
            if errors:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect("/")
            else:
                update_show = NewShow.objects.get(id=show_id)
                update_show.title = request.POST['title']
                update_show.network = request.POST['network']
                update_show.release = request.POST['release']
                update_show.desc = request.POST['desc']
                update_show.save()
                return redirect(f"show_info/{show.id}")






