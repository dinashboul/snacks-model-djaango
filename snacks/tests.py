from django.urls import reverse
from django.test import SimpleTestCase
from django.test import TestCase

# Create your tests here.
class thingsTests(TestCase):
    def test_home_page_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        # print(response)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)
        self.assertTemplateUsed(response,'snacks.html')  