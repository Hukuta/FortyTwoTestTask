""" Tests for Tasks """
import re
import json
from datetime import date
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
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
        """ Test ajax request """
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

    def test_template_usage(self):
        """ Test correct template """
        page = self.client.get(reverse('requests'))
        self.assertTemplateUsed(page, 'requests.html')


class EditPage(TestCase):
    """ Test edit Person Profile page  """

    def setUp(self):
        # create test user
        self.tester = 'tester'
        User.objects.create_user(self.tester, 'test@test.com',
                                 self.tester)

    def test_need_auth(self):
        """ Only logged in user cat see form """
        before = self.client.get(reverse('edit_data'))
        self.client.login(username=self.tester, password=self.tester)
        after = self.client.get(reverse('edit_data'))
        form_before = before.context['form']
        form_after = after.context['form']
        self.assertIsNone(form_before.initial.get('first_name'))
        self.assertIsNotNone(form_after.initial.get('first_name'))

    def test_edit_page_data(self):
        """ Testing initial data from context """
        self.client.login(username=self.tester, password=self.tester)
        page = self.client.get(reverse('edit_data'))
        form = page.context['form']
        person = Person.objects.get(pk=1)
        for field in person._meta.get_all_field_names():
            self.assertEqual(form.initial[field],
                             getattr(person, field))

    def test_ajax_post(self):
        """ Testing ajax request saves changes """
        self.client.login(username=self.tester, password=self.tester)
        person = Person.objects.get(pk=1)
        self.client.post(reverse('edit_data'))
        ajax_post = {
            'first_name': 'firstname',
            'last_name': 'lastname',
            # date mistake
            'date_of_birth': '1991-01-41',
            'contacts': 'contacts',
            'bio': 'bio',
            # email mistake
            'email': 'email@email',
            'jabber': 'email@email.ru',
            # empty field
            'skype': '',
        }
        self.client.post(reverse('edit_data'), ajax_post)
        person = Person.objects.get(pk=1)
        for field in ('date_of_birth', 'email', 'skype'):
            self.assertNotEqual(getattr(person, field),
                                ajax_post[field])
        ajax_post['date_of_birth'] = '1991-01-01'
        ajax_post['email'] = 'email@email.ru'
        ajax_post['skype'] = 'skypeid'
        self.client.post(reverse('edit_data'), ajax_post)
        person = Person.objects.get(pk=1)
        for field in ajax_post.keys():
            value = getattr(person, field)
            if isinstance(value, date):
                value = value.strftime("%Y-%m-%d")
            self.assertEqual(value, ajax_post[field])
