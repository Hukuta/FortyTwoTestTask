# -*- coding: utf-8 -*-
from south.v2 import SchemaMigration
from django.core.management import call_command


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding data for model 'Person'
        call_command('loaddata', 'user_data.json')

    def backwards(self, orm):
        # do nothing
        pass
