from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RecipePost, RecipeComment


@admin.register(RecipePost)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'ingredients', 'type_of_cuisine', 'dietary_categories',]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions',)


# Register your models here.
admin.site.register(RecipeComment)
