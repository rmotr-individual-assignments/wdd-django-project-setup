from django.test import TestCase


class ViewsTestCase(TestCase):

    def test_hello_world_view(self):
        response = self.client.get('/accounts/hello-world')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'Hello World!')
