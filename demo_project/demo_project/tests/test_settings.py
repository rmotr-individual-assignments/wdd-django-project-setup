from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):

    def test_required_setting_exists(self):
        self.assertTrue(hasattr(settings, 'NEW_SETTING'))
        self.assertEqual(settings.NEW_SETTING,
                         'This is my first Django project')
