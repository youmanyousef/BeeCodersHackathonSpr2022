from django.db import models

# Create your models here.
# student/user data tables
#class User(models.Model):
    # Unique primary ID (key)
    # Name field
    # College/School Field
    # Classes/Equivalent Field
    # Bio
    # Interests (misc, not needed) 
    # Projects Followed
    # Projects Started
    # Friends (misc, not needed)

# Project Listing data tables
#class Projects(models.Model):
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