from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# student/user data tables
class StudentUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.CharField(max_length=60) # Create separate table with colleges and serve recommendations based on existing colleges in db?
    biography = models.CharField(max_length=200)
    projects = models.ManyToManyField("Project")
    # Unique primary ID (key)
    # Name field                        -- done
    # College/School Field              -- done 
    # Classes/Equivalent Field
    # Bio                               -- done
    # Interests (misc, not needed) 
    # Projects Followed                 -- done 
    # Projects Started                  -- done, projects started will be tracked through author field in project model
    # Friends (misc, not needed)

# Project Listing data tables
class Project(models.Model):
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200, blank=True)
    # Unique primary ID (key)
    # Post field (possibly a json object with
        ## Project Name
        ## Student Name
        ## Subject
        ## Body
        ## Date
        ## Edited dates (probably not needed)

    # Thread/Comments (possibly a json objecet with
        ## All comments
            ### Student Name
            ### Comment
            ### Comment like count (probably not needed)
            ### is Followed? boolean
    # is Complete? boolean
    # Followers (list of followed Students IDs)

class Comment(models.Model):
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.CharField(max_length=300) 