from django import forms
from .models import FeedbackForm


class FeedbackForm(forms.ModelForm):
    """
    Form class for users to send feedbacks
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = FeedbackForm
        fields = ('name', 'email', 'message')