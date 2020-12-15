from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
   
    return render(request, 'index.html')## renders the origiinal html page  

def shows(request): # this function is for my table of items in the db 
    context = {
        "all_shows": NewShow.objects.all()#says i want all items o the model NewShow
    }

    return render(request, 'shows.html', context)

def add_show(request):#this method creates a new model element 
    if request.method == "POST":
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
    show.delete()
    return redirect('/shows')

def edit_show(request, show_id):
    context = {
    'show': NewShow.objects.get(id=show_id),
    'all_shows': NewShow.objects.all()
        
    }
    return render(request, 'edit.html', context)

def show_update(request, show_id):
    update_show = NewShow.objects.get(id=show_id)
    update_show.title = request.POST['title']
    update_show.network = request.POST['network']
    update_show.release = request.POST['release']
    update_show.desc = request.POST['desc']
    update_show.save()
    return redirect(f"show_info/{show.id}")






