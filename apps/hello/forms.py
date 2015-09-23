#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from apps.hello.models import Person

__author__ = 'Odarchenko N.D.'


class PickMeUpWidget(forms.DateInput):
    # Date Picker Widget
    class Media:
        # required media files
        css = {
            'all': ('css/pickmeup.min.css',)
        }
        js = ('js/jquery.pickmeup.min.js',)

    format = "%d.%m.%Y"

    def __init__(self, attrs=None):
        super(PickMeUpWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        value = value.strftime(self.format)
        rendered = forms.DateInput(attrs=attrs).render(name, value)
        params = "format: '" + self.format.replace('%', '') + "'"
        params += ", default_date: '%s'" % value
        script = u'''<script type="text/javascript">
                     $('#id_%s').pickmeup({%s});
                     </script>''' % (name, params)
        return rendered + mark_safe(script)


class ProfileForm(forms.ModelForm):
    # Person profile edit form

    widget = PickMeUpWidget()
    date_of_birth = forms.DateField(widget=widget)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False

    class Meta:
        model = Person
