from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


    
class HomeTemplateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_home_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app1/home.html')
        self.assertContains(response, '<title>Home Page</title>')
        self.assertContains(response, '<h1>Welcome</h1>')
        self.assertContains(response, '<div class="slideshow">')
        self.assertInHTML('<img src="/static/images/curry.jpg">', response.content.decode())
        self.assertInHTML('<img src="/static/images/mahomes.jpg">', response.content.decode())
        self.assertInHTML('<img src="/static/images/jesss.jpg">', response.content.decode())
        self.assertInHTML('<img src="/static/images/izzy.jpg">', response.content.decode())
        self.assertInHTML('<img src="/static/images/messi.jpg">', response.content.decode())
        self.assertInHTML('<img src="/static/images/hockey.jpg">', response.content.decode())

    def test_homepage_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'app1/home.html')

    def test_homepage_context(self):
        # test other context variable
        response = self.client.get(self.url)
        self.assertEqual(response.context['title'], 'Home Page')

    def test_homepage_html(self):
        # test other HTML elements as needed
        response = self.client.get(self.url)
        self.assertContains(response, '<html>')
        self.assertContains(response, '<title>Home Page</title>')




class NavigationTestCase(TestCase):
    
    def test_links(self):
        response = self.client.get(reverse('home'))
        html_content = response.content.decode('utf-8')
        self.assertInHTML('<a href="/basketball/">Basketball</a>', html_content)
        self.assertInHTML('<a href="/baseball/">Baseball</a>', html_content)
        self.assertInHTML('<a href="/hockey/">Hockey</a>', html_content)
        self.assertInHTML('<a href="/news/">News</a>', html_content)
        self.assertInHTML('<a href="/trending/">Trending</a>', html_content)



class ContactFormTestCase(TestCase):
    def test_contact_form_submission(self):
        # Submit a contact form with test data
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'This is a test message.',
        })

        # Check that the form submission was successful
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for your message.')

        # Check that an email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Contact Form Submission')
        self.assertEqual(
            mail.outbox[0].body, 'Name: Test User\nEmail: testuser@example.com\nMessage: This is a test message.')
