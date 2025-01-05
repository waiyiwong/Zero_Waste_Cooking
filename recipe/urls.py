from django.urls import path
from .views import (
    RecipePostList,
    AddRecipe,
    EditRecipe,
    DeleteRecipe,
    recipe_post_detail,
    recipe_comment_edit,
    recipe_comment_delete,
)


urlpatterns = [
    path('', RecipePostList.as_view(), name='recipe'),
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path('<slug:slug>/', recipe_post_detail, name="recipe_post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         recipe_comment_edit, name='recipe_comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         recipe_comment_delete, name='recipe_comment_delete'),
]
