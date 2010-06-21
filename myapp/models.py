from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models import permalink

class CustomUser(User):
    objects = UserManager()

    @property
    def display_name(self):
        if self.first_name:
            name = self.first_name
        else:
            name = self.email
        return name
    
    def __unicode__(self):
        return self.email
    
    @permalink
    def get_absolute_url(self):
        return ("user", (self.id,))


