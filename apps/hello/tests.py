""" Test for Task 1 """
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from apps.hello.admin import AdminPersons
from apps.hello.models import Person


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

    def test_template_usage(self):
        """ Test correct template used """
        self.assertTemplateUsed(self.client.get(reverse('home')),
                                'index.html')


class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True


request = MockRequest()
request.user = MockSuperUser()


class AdminActions(TestCase):
    """ Test for adminCP """

    def setUp(self):
        self.app_admin_persons = AdminPersons(Person, AdminSite())
        self.tester = 'admin'
        User.objects.create_superuser(self.tester, 'admin@test.com',
                                      self.tester)

    def test_person_update_form(self):
        """ Test person form in adminCP """
        need_fields = ['first_name', 'last_name', 'date_of_birth',
                       'contacts', 'bio', 'email', 'jabber', 'skype']
        base_fields = self.app_admin_persons.get_form(request).base_fields
        self.assertEqual(list(base_fields), need_fields)

    def test_admin_cp_is_available(self):
        """ Test admin CP is available for login """
        self.client.logout()
        self.assertContains(self.client.get('/admin/'), 'Log in')
        self.client.login(username=self.tester, password=self.tester)
        self.assertNotContains(self.client.get('/admin/'), 'Log in')

    def test_person_edit_form(self):
        """ Test edit form loading for update person """
        person = Person.objects.get(pk=1)
        self.client.login(username=self.tester, password=self.tester)
        page_uri = '/admin/hello/person/1/'
        page = self.client.get(page_uri)
        self.assertEqual(page.context['fieldset'].form.instance, person)
