from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # should display a form with 'project_title' and 'project_desc', fields
    # should perform POST request with 'project_title' and 'project_desc'
    path('project/create', views.create, name='create'),
    # should display form with 'username' input field and 
    # 'password' input field, should perform post request
    path('login', views.login_view, name='login'),
    # no front end needed 
    path('logout', views.logout, name='logout'),
    # no front end needed
    path('project/delete/<uuid:id>', views.delete, name='delete'),
    # should display grid of projects request.user has created,
    # projects should be links to 'project/delete/<uuid>'
    # then should display toast or banner with success method
    path('project/delete', views.delete_page, name='delete_page')
]