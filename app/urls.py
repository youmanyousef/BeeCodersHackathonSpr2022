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
    path('logout', views.logout_view, name='logout'),
    
    # should display form with input fields 'username' 'password' 'confirmation'
    # 'school' 'biography'-- submit button should perform post
    # request with these values
    path('register', views.register, name='register'),

    # no front end needed
    path('project/delete/<uuid:id>', views.delete, name='delete'),

    # project page
    path('project/<uuid:id>', views.project, name='project'),

    # should display grid of projects request.user has created,
    # projects should be links to 'project/delete/<uuid>'
    # then should display toast or banner with success method
    path('project/delete', views.delete_page, name='delete_page')
]