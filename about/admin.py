from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, FeedbackForm


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)


@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)
