"""My models"""
import os
from django.db import models
from PIL import Image


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
    photo = models.ImageField(upload_to='photo', null=True, default=None)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=True):

        super(Person, self).save()
        if self.photo:
            filename = self.photo.path
            try:
                image = Image.open(filename)
                width, height = image.size
                if width > 200 or height > 200:
                    image.thumbnail((200, 200), Image.ANTIALIAS)
                    image.save(filename)
                if not os.path.isdir('assets/photo'):
                    os.mkdir('assets/photo', 0777)
                target = 'assets/photo/' + filename.split('/')[-1]
                if not os.path.isfile(target):
                    os.symlink(filename, target)
            except IOError as err:
                print err
                self.photo = None
                super(Person, self).save()

    def get_img_url(self):
        try:
            return self.photo.url.replace('uploads/', 'static/')
        except ValueError:
            # 1 px transparent image
            return '/static/img/no_image.png'


class Req(models.Model):
    # HTTP Requests
    info = models.TextField()
    read = models.BooleanField(default=False)

    def __unicode__(self):
        return self.info


class EntryChange(models.Model):
    """ Logging all changes in models """
    action = models.CharField(max_length=7)
    time = models.DateTimeField(auto_now=True, auto_now_add=True)
    model = models.CharField(max_length=30)
