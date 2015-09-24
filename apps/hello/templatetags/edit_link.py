#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

__author__ = 'Odarchenko N.D.'

register = template.Library()


@register.simple_tag
def edit_link(obj):
    obj_ct = ContentType.objects.get_for_model(obj.__class__)
    url = 'admin:%s_%s_change' % (obj_ct.app_label, obj_ct.name)
    return reverse(url, args=(obj.id,))
