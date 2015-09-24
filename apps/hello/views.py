""" Views """
import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from apps.hello.models import Person, Req
from apps.hello.forms import ProfileForm


def index(request):
    """ My Profile Data Page """
    my_data = Person.objects.get(pk=1)
    return render(request, 'index.html', dict(person=my_data))


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


def edit(request):
    """ My Profile Data Edit Page """

    my_data = Person.objects.get(pk=1)

    if request.user.is_authenticated():
        # for authenticated users
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES,
                               instance=my_data)
            resp = dict(ok=0)
            if form.is_valid():
                form.save()
                resp['ok'] = 1
                resp['image'] = my_data.get_img_url()
            else:
                errors = dict()
                for error in form.errors:
                    errors[error] = form.errors[error]
                resp['errors'] = errors
            return HttpResponse(json.dumps(resp))
        else:
            form = ProfileForm(instance=my_data)
            return render(request, 'edit.html', dict(form=form))
    else:
        # for anonymous users
        return auth_views.login(request, template_name='edit.html',
                                redirect_field_name='next')
