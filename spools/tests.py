from django.core.urlresolvers import reverse
from django.test import TestCase

from spools.models import Spool, Thumper

def create_thumper(content_text, image):
    return Thumper.objects.create(
        spool=Spool.objects.create(),
        content_text=content_text,
        image=image
    )

class ThumperMethodTests(TestCase):

    def test_empty_thumper(self):
        """
        If the thumper has no spools, raise an exception.
        """
        full_thumper = create_thumper('hi', 'image.jpg')
        self.assertTrue(full_thumper.is_valid())

        empty_thumper = create_thumper('', '')
        self.assertFalse(empty_thumper.is_valid())

class SpoolViewTests(TestCase):

    def test_index_view_with_no_polls(self):
        """
        If no spools exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('spools:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No spools.")
        self.assertQuerysetEqual(response.context['latest_spool_list'], [])

    def test_index_view_with_a_spool(self):
        """
        Spools should be displayed on the index page.
        """
        Spool.objects.create(subject="Hello")
        response = self.client.get(reverse('spools:index'))
        self.assertQuerysetEqual(
            response.context['latest_spool_list'],
            ['<Spool: Hello>']
        )
