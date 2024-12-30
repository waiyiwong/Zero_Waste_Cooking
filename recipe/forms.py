from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'featured_image',
                'ingredients', 'instructions', 'type_of_cuisine',
                'dietary_categories', 'status']
        widgets = {
            'type_of_cuisine': forms.RadioSelect,
            'dietary_categories': forms.RadioSelect,
        }
        

class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('body',)