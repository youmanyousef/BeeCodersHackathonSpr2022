from django.contrib import admin
from .models import StudentUser, Project, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_time')

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)