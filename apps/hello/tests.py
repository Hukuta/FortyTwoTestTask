""" Tests for Tasks """
import re
import json
from django.core.urlresolvers import reverse
from django.test import TestCase
from apps.hello.models import Person
from apps.hello.models import Req


class IndexPage(TestCase):
    """ Test for IndexPage """
    def test_main_page(self):
        """ Test that home page is available
            and contains my personal data
        """
        page = self.client.get(reverse('home'))
        self.assertEqual(page.status_code, 200)
        data = ['Nikita', 'Odarchenko',
                '02.02.1992', 'odarchenko.n.d@gmail.com']
        for search_str in data:
            self.assertContains(page, search_str, 1)

    def test_unicode_render(self):
        """ Test __unicode__ method of model.Person """
        person = Person.objects.get(pk=1)
        full_name = repr(person)
        self.assertTrue(person.first_name in full_name)

    def test_page_title(self):
        """ page title should start with (N) N=new requests """
        self.client.get(reverse('home'))
        page = self.client.get(reverse('requests'))
        self.assertContains(page, '<title>(', 1)
        match = re.search('<title>\(([^<]+)\)([^<]+)</', page.content)
        self.assertIsNotNone(match)
        # requests > 0
        self.assertGreater(int(match.group(1)), 0)

    def test_middleware(self):
        """ Test adding data to database """
        count_before = Req.objects.count()
        self.client.get(reverse('home'))
        count_after = Req.objects.count()
        self.assertGreater(count_after, count_before)

    def test_ajax(self):
        self.client.get(reverse('home'))
        count_before = Req.objects.count()
        ajax = self.client.get(
            reverse('requests'),
            {'read': []},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        count_after = Req.objects.count()
        self.assertEqual(count_before, count_after)
        data = json.loads(ajax.content.decode())
        self.assertGreater(int(data['total']), 0)
        self.assertTrue('requests' in data)
        self.assertGreaterEqual(data['total'], len(data['requests']))
