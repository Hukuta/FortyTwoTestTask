""" Views """
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from apps.hello.models import Person


def index(request):
    """ My Profile Data Page """
    my_data = Person.objects.get(pk=1)
    return render_to_response('index.html', dict(person=my_data))


def requests(request):
    """ My Profile Data Page """
    data = {
        # TODO: implement this view
        'requests': [],
        'total': 0
    }
    if request.is_ajax():
        data = serializers.serialize("json", data)
        return HttpResponse(data, content_type="application/json")
    else:
        return render_to_response('requests.html', data)
