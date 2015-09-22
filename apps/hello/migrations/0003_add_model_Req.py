# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Req'
        db.create_table(u'hello_req', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('read', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'hello', ['Req'])


    def backwards(self, orm):
        # Deleting model 'Req'
        db.delete_table(u'hello_req')


    models = {
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'contacts': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hello.req': {
            'Meta': {'object_name': 'Req'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['hello']