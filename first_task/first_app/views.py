from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MyModel

def index(request):
    return HttpResponse("Hello, world!")

# Эндпоинт для задачи 2 (пока просто возвращает текст)
def get1(request):
    return HttpResponse("GET Endpoint 1")

def get2(request):
    return HttpResponse("GET Endpoint 2")

def post1(request):
    return HttpResponse("POST Endpoint 1")

# Эндпоинт для POST и GET с редиректом
def combined(request):
    if request.method == 'POST':
        new_model = MyModel(name="New Name", description="New Description")
        new_model.save()
        return HttpResponseRedirect(reverse('success'))
    else:
        return HttpResponse("This is a GET request")

def success(request):
    return HttpResponse("Success!")
