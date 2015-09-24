#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" URLs for this app """
import apps.hello.signals
from django.conf.urls import url, patterns
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

__author__ = 'Odarchenko N.D.'

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='home'),
    url(r'^requests$', views.requests, name='requests'),
    url(r'^edit$', views.edit, name='edit_data'),

)

urlpatterns += staticfiles_urlpatterns()
