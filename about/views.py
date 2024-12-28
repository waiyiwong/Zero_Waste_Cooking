from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import FeedbackForm


def about_us(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.add_message(request, messages.SUCCESS, "Your feedback has been submitted. Thank you!")

    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    feedback_form = FeedbackForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
        "feedback_form": feedback_form,
    },
    )
