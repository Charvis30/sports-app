from django.test import TestCase, Client
from django.urls import reverse

class NewsTemplateTestCase(TestCase):
    def test_news_template(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news.html')
        self.assertContains(response, '<title>What You Missed</title>')
        self.assertContains(response, '<h2>scores(api will go here)</h2>')
        self.assertContains(response, '<td>Memphis Grizz</td>')
        self.assertContains(response, '<td>Los Angeles Lakers</td>')
        self.assertContains(response, '<td>105 - 109</td>')
        self.assertContains(response, '<td>Miami Heat</td>')
        self.assertContains(response, '<td>Phoenix Suns</td>')
        self.assertContains(response, '<td>100 - 89</td>')

class TrendingTemplateTestCase(TestCase):
    def test_trending_template(self):
        response = self.client.get('/trending/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/trending.html')
        self.assertContains(response, '<title>What You Missed</title>')
        self.assertContains(response, '<h2>feeds/news(api will go here)</h2>')
        self.assertContains(response, '<p>westbrook traded to clippers.....</p>')
        self.assertContains(response, '<p>twitter feed </p>')

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
        self.assertContains(response, '<img src="{% static \'images/curry.jpg\' %}">')
        self.assertContains(response, '<img src="{% static \'images/mahomes.jpg\' %}">')
        self.assertContains(response, '<img src="{% static \'images/jesss.jpg\' %}">')
        self.assertContains(response, '<img src="{% static \'images/izzy.jpg\' %}">')
        self.assertContains(response, '<img src="{% static \'images/messi.jpg\' %}">')
        self.assertContains(response, '<img src="{% static \'images/hockey.jpg\' %}">')

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

    def test_homepage_links(self):
        # test other links as needed
        response = self.client.get(self.url)
        self.assertContains(response, '<a href="#about">About</a>')
        self.assertContains(response, '<a href="#contact">Contact</a>')



