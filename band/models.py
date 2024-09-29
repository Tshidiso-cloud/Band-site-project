# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Represents an event.

    This model stores information about an event, 
    including its title, date, description, and the 
    user who created it.
    """
    # The title of the event, stored as a string with a 
    # maximum length of 100 characters.
    title = models.CharField(max_length=100)
    
    # The date and time of the event.
    date = models.DateTimeField()
    
    # A detailed description of the event.
    description = models.TextField()
    
    # The user who created the event, with a foreign key 
    # relationship to the User model.
    # When the related User is deleted, all associated 
    # Event objects will also be deleted.
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        '''
        Returns the title of the event when the object is printed or 
        converted to a string. This returns the title of the event,
        this is an extra docstring for git.
        '''
        return self.title
