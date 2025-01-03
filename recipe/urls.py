from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipePostList.as_view(), name='recipe'),
    path('<slug:slug>/', views.recipe_post_detail, name="recipe_post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.recipe_comment_edit, name='recipe_comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.recipe_comment_delete, name='recipe_comment_delete'),
]
