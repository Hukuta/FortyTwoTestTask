from django.contrib import admin
from apps.hello.models import Person, Req


class AdminPersons(admin.ModelAdmin):
    """ Persons model admin  """
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email',
                    'jabber', 'skype', 'contacts', 'bio', 'photo')


class AdminRequests(admin.ModelAdmin):
    """ HTTP Requests log model admin  """
    list_display = ('info', 'read', 'priority',)


admin.site.register(Person, AdminPersons)
admin.site.register(Req, AdminRequests)
