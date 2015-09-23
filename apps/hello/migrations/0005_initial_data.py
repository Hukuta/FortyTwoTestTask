# -*- coding: utf-8 -*-
from django.db import OperationalError
from south.v2 import SchemaMigration
from django.core.management import call_command


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding data for model 'Person'
        try:
            call_command('loaddata', 'user_data.json')
        except OperationalError as er:
            print er


    def backwards(self, orm):
        # do nothing
        pass
