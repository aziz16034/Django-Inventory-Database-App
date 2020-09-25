from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render (request, 'index.html')
    

def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items' : items,
        'context': 'Laptop'
    }

    return render(request, 'index.html', context)



def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items' : items,
        'header': 'Mobile'
    }

    return render(request, 'index.html', context)



def display_phone(request):
    items = phone.objects.all()
    context = {
        'items' : items,
        'context': 'phone'
    }

    return render(request, 'index.html', context)



def add_item(request, cls):
    if request.method =="POST":
        form = cls(request.POST)
        
        if form.is_valid():
            form.save
            return redirect('index')




    else:
        form = cls()
        return render(request,'add_new.html', {'form':form})



def add_laptop(request):
    return add_item(request, LaptopForm)


def add_Mobile(request):
    return add_item(request, MobileForm)


def add_phone(request):
    return add_item(request, phoneForm)



def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_Laptop(request, pk):
    return edit_item (request, pk, Laptop, LaptopForm)


def edit_Mobile(request, pk):
    return edit_item(request, pk, Mobile, MobileForm)


def edit_phone(request, pk):
    return edit_item(request, pk, phone, phoneForm)





def delete_Laptop(request, pk):

    template = 'index.html'
    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Mobile(request, pk):

    template = 'index.html'
    Mobile.objects.filter(id=pk).delete()

    items = Mobile.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_phone(request, pk):

    template = 'index.html'
    phone.objects.filter(id=pk).delete()

    items = phone.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

