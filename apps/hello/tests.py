from django.core.urlresolvers import reverse
from django.test import TestCase


class IndexPage(TestCase):
    def test_main_page(self):
        page = self.client.get(reverse('home'))
        self.assertEqual(page.status_code, 200)
        data = ['Nikita', 'Odarchenko', '02.02.1992', 'odarchenko.n.d@gmail.com']
        for s in data:
            self.assertContains(page, s, 1)