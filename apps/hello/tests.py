""" Test for Task 1 """
from django.core.urlresolvers import reverse
from django.test import TestCase


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
