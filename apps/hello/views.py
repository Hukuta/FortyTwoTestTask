""" Views """
from django.shortcuts import render_to_response


def index(request):
    """ My Profile Data Page """
    return render_to_response('index.html')
