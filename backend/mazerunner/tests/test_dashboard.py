from django.http import request, HttpRequest, response
from django.template import RequestContext, context
from django.template.loader import render_to_string
from api.views import overallSummaryView
from django.contrib.auth import get_user_model
from django.test import TestCase

def setUp(self):
    """ Create a student account """
    self.student = get_user_model().objects.create_user(
        email='SGX@123.com',
        password='11111111',
        name='sgx',
        distanceToNPC=0,
        overallScore=0,
        containBonus=False
    )
def test_template(self):
    self.assertTemplateUsed(self.response, 'dashboard.html')

def test_has_view(self):
    overallView = overallSummaryView
    view = self.response.context['overallView']
    expected_html = render_to_string('dashboard.html', context)
    self.assertEqual(view, expected_html)
