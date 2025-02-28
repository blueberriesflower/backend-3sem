from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MyModel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from .models import CustomUser 

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

def user_create(request): #POST
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            email = data['email']
            password = data['password']
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'message': 'User created successfully', 'id': user.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

def user_detail(request, user_id): #GET
    user = get_object_or_404(CustomUser, pk=user_id)
    data = {'id': user.id, 'username': user.username, 'email': user.email}
    return JsonResponse(data)

def user_update(request, user_id): #PUT/PATCH
   if request.method == 'PUT':
       try:
           user = get_object_or_404(CustomUser, pk=user_id)
           data = json.loads(request.body)
           user.username = data.get('username', user.username)
           user.email = data.get('email', user.email)
           user.save()
           return JsonResponse({'message': 'User updated successfully'})
       except Exception as e:
           return JsonResponse({'error': str(e)}, status=400)
   else:
       return JsonResponse({'error': 'Invalid method'}, status=400)
   
def user_delete(request, user_id): #DELETE
    if request.method == 'DELETE':
        try:
            user = get_object_or_404(CustomUser, pk=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)
    