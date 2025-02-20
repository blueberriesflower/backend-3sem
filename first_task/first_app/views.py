from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MyModel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

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


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
