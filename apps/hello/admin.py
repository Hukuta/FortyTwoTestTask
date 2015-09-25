from django.contrib import admin
from apps.hello.models import Person


class AdminPersons(admin.ModelAdmin):
    """ Persons model admin  """
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email',
                    'jabber', 'skype', 'contacts', 'bio', 'photo')


admin.site.register(Person, AdminPersons)
