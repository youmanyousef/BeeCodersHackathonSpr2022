from django.contrib import admin
from .models import StudentUser, Project

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Project)