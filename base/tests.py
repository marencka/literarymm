from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, dashboard, meditation, pdpr, history, information, pdpr_history
from base.forms import PDPRForm, ReflectionForm
from base.models import Quote, PDPR


# URL tests for base/views.py:
# 7 tests in total

class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, home)

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)
    
    def test_meditation_url_resolves(self):
        url = reverse('meditation')
        self.assertEquals(resolve(url).func, meditation)

    def test_pdpr_url_resolves(self):
        url = reverse('pdpr')
        self.assertEquals(resolve(url).func, pdpr)
    
    def test_history_url_resolves(self):
        url = reverse('history')
        self.assertEquals(resolve(url).func, history)
    
    def test_information_url_resolves(self):
        url = reverse('information')
        self.assertEquals(resolve(url).func, information)
    
    def test_pdpr_hisotry_url_resolves(self):
        url = reverse('pdpr_history')
        self.assertEquals(resolve(url).func, pdpr_history)

# Test forms:
# 4 tests in total

    def test_reflection_valid(self):
        form = ReflectionForm(data = {
            'text': 'adjksf'
        })
        self.assertTrue(form.is_valid())

    def test_reflection_invalid(self):
        form = ReflectionForm(data={})

        self.assertFalse(form.is_valid())

    def test_pdpr_valid(self):
        form = PDPRForm(data = {
            'q1': 1,
            'q2': 1,
            'q3': 1,
            'q4': 1,
            'q5': 1,
            'q6': 1,
            'q7': 1,
            'q8': 1,
            'q9': 1,
            'q10': 1,
            'q11': 1,
            'q12': 1,
            'q13': 1,
            'q14': 1,
            'q15': 1
        })
        self.assertTrue(form.is_valid())
    
    def test_pdpr_invalid(self):
        form = PDPRForm(data={})
    
        self.assertFalse(form.is_valid())

# quote tests:
# 2 in total

class TestModels(TestCase):
    def setUp(self):
        self.q1 = Quote.objects.create(
            quote = 'quote',
            author = 'hi'
        )

    def test_random_quote(self):
        self.assertEquals(self.q1.quote, 'quote')

    def test_random_quote_author(self):
        self.assertEquals(self.q1.author, 'hi')

    
    
  


    

