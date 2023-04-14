from django.shortcuts import render , redirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    item = Item.objects.all()[2]
    context = {'item':item}  
    return render(request,'core/home.html', context)

def mens(request):
    mens = Men.objects.all()
    context = {'mens':mens}
    return render(request, 'core/mens.html', context)

def womens(request):
    womens = Women.objects.all()
    context = {'womens':womens}
    return render(request, 'core/womens.html', context)
    

def trending(request):
    items = Item.objects.all()
    context = {'items':items}  
    return render(request,'core/trending.html', context)

# CRUD: CREATE ITEM
def add_item(request):
    form = Menform()
    if request.method =='POST':
        form = Menform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mens')
    context = {'form': form}
    return render(request,'core/add_item.html', context)

def add_women_item(request):
    form = Womenform()
    if request.method == 'POST':
        form = Womenform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('womens')
    context = {'form': form}
    return render(request,'core/add_womens_item.html', context)



        
# CRUD: DELETE ITEM
def delete_item(request, id):
    item =  Men.objects.get(id=id)
    item.delete()
    return redirect('mens')

def delete_women_item(request,id):
    item = Women.objects.get(id=id)
    item.delete()
    return redirect('womens')

# CRUD: UPDATE ITEM
def update_item(request, id):
    item = Men.objects.get(id=id)
    form = Menform(instance=item)
    if request.method == 'POST':
        form = Menform(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('mens')
    context = {'form': form}
    return render(request,'core/add_item.html', context)

def update_women_item(request,id):
    item = Women.objects.get(id=id)
    form = Womenform(instance=item)
    if request.method == 'POST':
        form = Womenform(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('womens')
    context = {'form': form}
    return render(request, 'core/add_womens_item.html', context)









    






    
