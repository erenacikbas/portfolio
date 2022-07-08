from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('resume')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'resume/index.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, '<title>Eren Tuna Açıkbaş</title>')
