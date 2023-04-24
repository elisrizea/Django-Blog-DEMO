from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .forms import ContactForm


class SupportViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('support')

    def test_get_support_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    from django.test import TestCase, Client
    from django.urls import reverse
    from django.core import mail
    from .forms import ContactForm

    class SupportViewTest(TestCase):

        def setUp(self):
            self.client = Client()
            self.url = reverse('support')

        def test_get_support_page(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'contact.html')
            self.assertIsInstance(response.context['form'], ContactForm)


        '''next test may work only when smtp email client is set
        def test_post_valid_form(self):
            form_data = {
                'subject': 'Test Subject',
                'from_email': 'test@example.com',
                'message': 'Test message',
            }
            with mail.outbox:
                response = self.client.post(self.url, form_data)
                self.assertRedirects(response, reverse('success'))
                self.assertEqual(len(mail.outbox), 1)
                self.assertEqual(mail.outbox[0].subject, 'Test Subject')
                self.assertEqual(mail.outbox[0].body, 'Test message')
                self.assertEqual(mail.outbox[0].from_email, 'test@example.com')
                self.assertEqual(mail.outbox[0].to, ['alin.rizea@gmail.com'])
'''

        def test_post_invalid_form(self):
            form_data = {
                'subject': '',
                'from_email': '',
                'message': '',
            }
            response = self.client.post(self.url, form_data)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'contact.html')
            self.assertFalse(response.context['form'].is_valid())

    def test_post_invalid_form(self):
        form_data = {
            'subject': '',
            'from_email': '',
            'message': '',
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFalse(response.context['form'].is_valid())
