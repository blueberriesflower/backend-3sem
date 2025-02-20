from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 


class CustomUserCreationForm(UserCreationForm):  # Для регистрации
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number')  # Добавляем email и phone_number