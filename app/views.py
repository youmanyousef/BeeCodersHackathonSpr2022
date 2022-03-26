from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("hello worlds!")
    user='yousef'
    context = {
        'user': user
    }
    return render(request, 'index.html', context=context)

def projects(request):
    return HttpResponse()