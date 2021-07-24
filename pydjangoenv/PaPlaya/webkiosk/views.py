from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

from .models import Customer, Food, Order
from .forms import FoodForm

def index(request):
    #return HttpResponse('<p>Welcom to the PaPlaya Web Kiosk</p>')
    return render(request, 'webkiosk/welcome.html')


def listfood(request):
    context = {
        'foodlist': Food.objects.all(),
        'testitem': 'chair'
    }
    return render(request, 'webkiosk/food.html', context)

def createfood(request):
    if request.method == 'GET':
        form = FoodForm()
    elif request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:food-list')


    context = {'form': form}
    return render(request, 'webkiosk/food_form.html', context)

def detailfood(request, pk):
    food = Food.objects.get(id=pk)
    context = {'food':food}
    return render(request, 'webkiosk/food_detail.html', context)

def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm (instance=food)

    elif request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updated.')
    context = {'form':form}
    return render(request, 'webkiosk/food_form.html', context)

def deletefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        context = {'food':food}
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
            food.delete()
            return redirect('webkiosk:food-list')
