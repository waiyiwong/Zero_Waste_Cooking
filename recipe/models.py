from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

CUISINE_TYPES = [
    ('British', 'British'),
    ('Italian', 'Italian'),
    ('Mexican', 'Mexican'),
    ('Indian', 'Indian'),
    ('Chinese', 'Chinese'),
    ('Japanese', 'Japanese'),
    ('French', 'French'),
    ('Mediterranean', 'Mediterranean'),
    ('Thai', 'Thai'),
    ('American', 'American'),
    ('Middle Eastern', 'Middle Eastern'),
    ('Other', 'Other'),
]

DIETARY_CATEGORIES = [
    ('Not-specify', 'Not-specify'),
    ('Vegan', 'Vegan'),
    ('Vegetarian', 'Vegetarian'),
    ('Gluten-Free', 'Gluten-Free'),
    ('Pescatarian', 'Pescatarian'),
    ('Dairy-Free', 'Dairy-Free'),
]


# Create your models here.
class RecipePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    type_of_cuisine = models.CharField(
        max_length=50,
        choices=CUISINE_TYPES,
        default='British'
    )
    dietary_categories = models.CharField(
        max_length=50,
        choices=DIETARY_CATEGORIES,
        default='Not-specify'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class RecipeComment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    recipe_post = models.ForeignKey(RecipePost, on_delete=models.CASCADE,
                                    related_name="recipe_comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
