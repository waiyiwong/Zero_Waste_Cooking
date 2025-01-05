from django import forms
from .models import RecipePost, RecipeComment


class RecipePostForm(forms.ModelForm):
    class Meta:
        model = RecipePost
        fields = ['title', 'slug', 'author', 'featured_image',
                  'ingredients', 'instructions', 'type_of_cuisine',
                  'dietary_categories', 'status']
        widgets = {
            'type_of_cuisine': forms.RadioSelect,
            'dietary_categories': forms.CheckboxSelectMultiple,
        }
        
        """ hide slug and status fields from user """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Hide 'slug' & 'author' field from form
        self.fields['slug'].widget = forms.HiddenInput()
        self.fields['author'].widget = forms.HiddenInput()

        # Conditionally hide 'status' field for non-admin users
        if not kwargs.get('instance') or not kwargs.get('instance').instance.author.is_staff:
            self.fields['status'].widget = forms.HiddenInput()  # Hide status for regular users

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Auto-generate the slug from the title if it's empty
        if not instance.slug:
            instance.slug = instance.title.lower().replace(" ", "-")
            
        # Set the author to the current logged-in user
        if not instance.author:
            instance.author = self.instance.request.user
        
        if commit:
            instance.save()
        
        return instance


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
