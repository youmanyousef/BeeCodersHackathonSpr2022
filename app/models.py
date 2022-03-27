from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

# Create your models here.
# student/user data tables
class StudentUser(AbstractUser):
    # Unique primary ID (key)
    # Name field                        -- done
    first_name = models.CharField(max_length=30)
    biography = models.CharField(max_length=200)
    # College/School Field              -- done 
    LANEY = 'LANEY'
    ALAMEDA = 'ALAMEDA'
    MERITT = 'MERITT'
    BERKELEY = 'BERKELEY'
    SCHOOL_CHOICES = [
        (LANEY, 'Laney College'),
        (ALAMEDA, 'College of Alameda'),
        (MERITT, 'Meritt College'),
        (BERKELEY, 'Berkeley City College')
    ]
    school = models.CharField(max_length=30, choices=SCHOOL_CHOICES) # Create separate table with colleges and serve recommendations based on existing colleges in db?
    # Classes/Equivalent Field
    classes = models.ManyToManyField("SubjectClass")
    # Bio                               -- done
    biography = models.CharField(max_length=200)
    # Interests (misc, not needed) 
    # Projects Followed                 -- done 
    # Projects Started                  -- done, projects started will be tracked through author field in project model
    projects = models.ManyToManyField("Project", blank=True)
    # Friends (misc, not needed)

class SubjectClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Project Listing data tables
class Project(models.Model):
    # Unique primary ID (key)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Post field (possibly a json object with
        ## Project Name
    title = models.CharField(max_length=80)
        ## Student Name
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
        ## Subject
        ## Body
    description = models.CharField(max_length=200, blank=True)
        ## Date
    date_time = models.DateTimeField()
        ## Edited dates (probably not needed)

    # Thread/Comments (possibly a json objecet with
        ## All comments
            ### Student Name
            ### Comment
            ### Comment like count (probably not needed)
            ### is Followed? boolean
    # is Complete? boolean
    complete = models.BooleanField(default=False)
    # Followers (list of followed Students IDs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.CharField(max_length=300) 

    def __str__(self):
        return f"{self.project} - {self.author}"