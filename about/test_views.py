from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import FeedbackForm


class TestAboutView(TestCase):
    def setUp(self):
        """Creates about us content"""
        self.about_content = About(
            title="About Us", content="This is about Zero Waste Cooking.")
        self.about_content.save()

    def test_render_about_page_with_feedback_form(self):
        """Verifies get request for about me containing a feedback form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.content)
        self.assertIsInstance(
            response.context['feedback_form'], FeedbackForm)

    def test_successful_feedback_request_submission(self):
        """Test for a user to send a feedback"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your feedback has been submitted. Thank you!', response.content)
