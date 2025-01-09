from django.test import TestCase
from .forms import RecipePostForm, RecipeCommentForm


# Create your tests here.
class TestRecipePostForm(TestCase):
    def test_recipe_form_is_valid(self):
        recipe_form = RecipePostForm({'title': 'Test Title',
                                      'ingredients': 'test ingredients',
                                      'instructions': 'test instructions 123',
                                      'type_of_cuisine': 'Thai',
                                      'dietary_categories': 'Vegan'})
        self.assertTrue(recipe_form.is_valid(), msg="Form is invalid")


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = RecipeCommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        comment_form = RecipeCommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
