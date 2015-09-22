""" Views """
import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from apps.hello.models import Person, Req


def index(request):
    """ My Profile Data Page """
    my_data = Person.objects.get(pk=1)
    return render_to_response('index.html', dict(person=my_data))


@csrf_exempt
def requests(request):
    """ My Profile Data Page """
    data = {
        'requests': [],
        'total': Req.objects.filter(read=False).count()
    }
    if request.is_ajax():
        read_ids = request.POST.getlist('ids[]')
        if read_ids:
            Req.objects.filter(pk__in=read_ids).update(read=True)
        requests_list = Req.objects.filter(read=False).order_by('pk')[:10]
        requests_json = serializers.serialize("json", requests_list)
        data['requests'] = json.loads(requests_json)
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return render_to_response('requests.html', data)
