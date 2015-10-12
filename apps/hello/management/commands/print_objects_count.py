#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db.models import get_apps, get_models
from django.db.utils import OperationalError

__author__ = 'Odarchenko N.D.'


class Command(BaseCommand):
    """ List all models with count of objects """
    help = 'List all models with count of objects'

    def handle(self, **options):
        """ exec command """
        for app in get_apps():
            for model in get_models(app):
                try:
                    objects_count = model.objects.count()
                except OperationalError as err:
                    self.stderr.write(err)
                    continue
                self.stdout.write('%s: objects: %s\n'
                                  % (model.__name__, objects_count))
                self.stderr.write('error: %s: objects: %s\n'
                                  % (model.__name__, objects_count))
