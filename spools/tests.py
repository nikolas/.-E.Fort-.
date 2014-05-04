from django.core.urlresolvers import reverse
from django.test import TestCase

from spools.models import SidebarItem, Spool, Thumper


class SidebarItemViewTests(TestCase):

    def test_sidebar_item_displays_on_index(self):
        """
        When an admin adds a sidebar item, it renders on the page.
        """
        SidebarItem.objects.create(content="My item!")
        response = self.client.get(reverse('spools:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My item!")


def create_thumper(content_text, image):
    return Thumper.objects.create(
        spool=Spool.objects.create(),
        content_text=content_text,
        image=image
    )

class ThumperMethodTests(TestCase):

    def test_empty_thumper(self):
        """
        A thumper without image or text is invalid.
        """
        empty_thumper = create_thumper('', '')
        self.assertFalse(empty_thumper.is_valid())

    def test_full_thumper(self):
        """
        A thumper with text or an image is valid
        """
        text_thumper = create_thumper('hi', '')
        self.assertTrue(text_thumper.is_valid())

        image_thumper = create_thumper('', 'image.jpg')
        self.assertTrue(image_thumper.is_valid())

        full_thumper = create_thumper('hi', 'image.jpg')
        self.assertTrue(full_thumper.is_valid())


class SpoolMethodTests(TestCase):

    def test_empty_spool(self):
        """
        A spool without any thumpers is not valid.
        """
        spool = Spool.objects.create()
        self.assertFalse(spool.is_valid())

    def test_invalid_spool(self):
        """
        A spool only invalid thumpers is invalid.
        """
        spool = Spool.objects.create()
        spool.thumper_set.add(Thumper.objects.create(spool=spool))
        self.assertFalse(spool.is_valid())

    def test_valid_spool(self):
        """
        A spool with at least one valid thumper is valid.
        """
        spool = Spool.objects.create()
        self.assertFalse(spool.is_valid())

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
