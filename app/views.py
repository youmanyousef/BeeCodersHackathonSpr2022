from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime

from .models import Project, StudentUser, SubjectClass

# Create your views here.
def index(request):
    context = {
        'projects': Project.objects.order_by('-date_time')[:10]
    }
    return render(request, 'index.html', context=context)

def project(request, id):
    try:
        project_obj = Project.objects.get(id=id)
        return render(request, 'project.html', {
            "title": project_obj.title,
            "description": project_obj.description,
            "author": project_obj.author,
            "date_time": project_obj.date_time,
            "image": project_obj.image,
            "id": project_obj.id,
            "tags": project_obj.tags.all(),
            'projects': Project.objects.order_by('-date_time')[:10]
        })
    except ObjectDoesNotExist:
        return render(request, 'index.html') # TODO IMPLEMENT 404 PAGE


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    if request.method == 'POST':
        title = request.POST.get('project_title')
        description = request.POST.get('project_desc')
        print(description)
        new_project = Project(title=title, description=description, author=request.user, date_time=datetime.now())
        new_project.save()

def delete(request, id):
    # get project from db with corresponding id
    project_obj = Project.objects.get(id=id)
    # delete only if the request user is the author of project
    if request.user == project_obj.author:
        print(project_obj)
        print(request.user)
        project_obj.delete()
        
    #todo implement else

def delete_page(request):
    # todo implement deletion page, offer projects user has created
    return render(request, 'index.html') #change template

def register(request):
    context = {
        'projects': Project.objects.order_by('-date_time')[:10],
        'subject_classes': SubjectClass.objects.order_by('name')
    }
    print(context)
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirmation = request.POST.get('confirmation')
        school = request.POST.get('school')
        
        if password != confirmation:
            #todo display error
            return HttpResponseRedirect(reverse('index'))
        biography = request.POST.get('biography')
        #attempt to create user
        try:
            user = StudentUser.objects.create_user(username, password)
            user.biography = biography
            user.last_name = last_name
            user.first_name = first_name
            user.school = school

            user.save()
        except IntegrityError:
            return render(request, 'register.html', {
                "error": "Username is already taken!" 
            })

        # Log in user, then redirect to home page
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        # render registration page
        return render(request, 'register.html', context=context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    if request.method == 'GET':
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def explore(request):
    context = {
        'projects': Project.objects.order_by('-date_time')[:10]
    }
    return render(request, 'explore.html', context=context)