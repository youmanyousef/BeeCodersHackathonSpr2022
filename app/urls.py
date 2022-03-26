from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/create', views.create, name='create'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('project/del/<int:id>', views.delete, name='delete'),

]