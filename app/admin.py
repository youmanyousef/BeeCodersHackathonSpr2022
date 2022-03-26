from django.contrib import admin
from .models import StudentUser, Project, Comment

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Project)
admin.site.register(Comment)