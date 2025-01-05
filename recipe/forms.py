from django import forms
from .models import RecipePost, RecipeComment


class RecipePostForm(forms.ModelForm):
    class Meta:
        model = RecipePost
        fields = ['title', 'featured_image',
                  'ingredients', 'instructions', 'type_of_cuisine',
                  'dietary_categories']
        widgets = {
            'type_of_cuisine': forms.RadioSelect,
            'dietary_categories': forms.RadioSelect,
        }


class RecipeCommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = RecipeComment
        fields = ('body',)
