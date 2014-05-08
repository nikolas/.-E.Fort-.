from django.core.urlresolvers import reverse
from django.test import TestCase

from spools.models import SidebarItem, Thumper


class SidebarItemViewTests(TestCase):

    def test_sidebar_item_displays_on_index(self):
        """
        When an admin adds a sidebar item, it renders on the page.
        """
        SidebarItem.objects.create(content="My item!")
        response = self.client.get(reverse('spools:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My item!")


class ThumperMethodTests(TestCase):

    def test_empty_thumper(self):
        """
        A thumper without image or text is invalid.
        """
        empty_thumper = Thumper.objects.create(content='', image='')
        self.assertFalse(empty_thumper.is_valid())

    def test_full_thumper(self):
        """
        A thumper with text or an image is valid
        """
        text_thumper = Thumper.objects.create(content='hi', image='')
        self.assertTrue(text_thumper.is_valid())

        image_thumper = Thumper.objects.create(content='', image='image.jpg')
        self.assertTrue(image_thumper.is_valid())

        full_thumper = Thumper.objects.create(content='hi', image='image.jpg')
        self.assertTrue(full_thumper.is_valid())


class ThumperViewTests(TestCase):

    def test_index_view_with_no_thumpers(self):
        """
        If no thumpers exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('spools:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No thumpers.")
        self.assertQuerysetEqual(response.context['latest_thumper_list'], [])

    def test_index_view_with_a_thumper(self):
        """
        Thumpers should be displayed on the index page.
        """
        Thumper.objects.create(content="Hello")
        response = self.client.get(reverse('spools:index'))
        self.assertQuerysetEqual(
            response.context['latest_thumper_list'],
            ['<Thumper: Hello>']
        )
