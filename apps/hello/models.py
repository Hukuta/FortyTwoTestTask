"""My models"""
from django.db import models


class Person(models.Model):
    """ information about person """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    contacts = models.TextField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Req(models.Model):
    # HTTP Requests
    info = models.TextField()
    read = models.BooleanField(default=False)

    def __unicode__(self):
        return self.info
