#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from apps.hello.models import Req

__author__ = 'Odarchenko N.D.'


class LogMiddleware(object):
    """ Middleware stores HttpRequest in DB """
    def process_response(self, request, response):
        # returns response as is

        if request.path != reverse('requests'):
            info = '%s %s\r\n%s' % (request.method, request.path,
                                    response.status_code)
            if Req.objects.filter(info=info, priority=1).count():
                priority = 1
            else:
                priority = 0
            Req(info=info, priority=priority).save()
        return response
