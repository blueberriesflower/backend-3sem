from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get1/', views.get1, name='get1'),
    path('get2/', views.get2, name='get2'),
    path('post1/', views.post1, name='post1'),
    path('combined/', views.combined, name='combined'),
    path('success/', views.success, name='success'),
]