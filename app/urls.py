from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find', views.find, name='find'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]