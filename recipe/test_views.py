from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .views import RecipePostList, AddRecipe
from .forms import RecipePostForm
from .models import RecipePost


# Create your tests here.
class RecipePostViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.user = User.objects.create_user(
            username="regular_Username",
            password="regular_Password",
            email="regularuser@test.com"
        )
        self.post = RecipePost(
            title="Test Recipe",
            slug="test-recipe",
            author=self.user,
            ingredients="test ingredients",
            instructions='test instructions: Step1, 2, 3',
            type_of_cuisine='Thai',
            dietary_categories='Vegan',
            status=1
            )
        self.post.save()

    def test_add_recipe_logged_in(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('add_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/add_recipe.html')
