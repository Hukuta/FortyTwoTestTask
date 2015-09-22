""" Views """
from django.shortcuts import render_to_response
from apps.hello.models import Person


def index(request):
    """ My Profile Data Page """
    my_data = Person.objects.get(pk=1)
    return render_to_response('index.html', dict(person=my_data))
