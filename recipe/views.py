from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RecipeCommentForm, RecipePostForm
from .models import RecipePost, RecipeComment
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.text import slugify
from django.db.models import Q
# Create your views here.


class RecipePostList(generic.ListView):
    """
    Returns all published recipe posts and handles search functionality.
    """
    model = RecipePost
    template_name = "recipe/recipe.html"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            recipe_search = RecipePost.objects.filter(
                Q(title__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(type_of_cuisine__icontains=query),
                status=1
            )
            if not recipe_search.exists():
                messages.info(self.request,
                              "No recipes found with the entered ingredients.")

        else:
            recipe_search = RecipePost.objects.filter(status=1)
        return recipe_search


def recipe_post_detail(request, slug):
    """
    Display an individual :model:`RecipePost`.

    **Context**

    ``recipe_post``
        An instance of :model:`RecipePost`.
    ``recipe_comments``
        All approved recipe_comments related to the recipe_post.
    ``recipe_comment_count``
        A count of approved recipe_comments related to the recipe_post.
    ``recipe_comment_form``
        An instance of :form:`recipe.RecipeCommentForm`

    **Template:**

    :template:`recipe/recipe_post_detail.html`
    """
    recipe_queryset = RecipePost.objects.filter(status=1)
    recipe_post = get_object_or_404(recipe_queryset, slug=slug)
    recipe_comments = recipe_post.recipe_comments.all().order_by("-created_on")
    recipe_comment_count = recipe_post.recipe_comments.filter(
        approved=False).count()
    if request.method == "POST":
        recipe_comment_form = RecipeCommentForm(data=request.POST)
        if recipe_comment_form.is_valid():
            recipe_comment = recipe_comment_form.save(commit=False)
            recipe_comment.author = request.user
            recipe_comment.recipe_post = recipe_post  # from line 66 models.py
            recipe_comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    recipe_comment_form = RecipeCommentForm()

    return render(
        request,
        "recipe/recipe_post_detail.html",
        {
            "recipe_post": recipe_post,
            "recipe_comments": recipe_comments,
            "recipe_comment_count": recipe_comment_count,
            "recipe_comment_form": recipe_comment_form
        },
    )


def recipe_comment_edit(request, slug, comment_id):
    """
    Display an individual recipe_comment for edit.

    **Context**

    ``recipe_post``
        An instance of :model:`recipe.RecipePost`.
    ``recipe_comment``
        A single recipe_comment related to the recipe_post.
    ``recipe_comment_form``
        An instance of :form:`recipe.RecipeCommentForm`
    """
    if request.method == "POST":

        recipe_queryset = RecipePost.objects.filter(status=1)
        recipe_post = get_object_or_404(recipe_queryset, slug=slug)
        recipe_comment = get_object_or_404(RecipeComment, pk=comment_id)
        recipe_comment_form = RecipeCommentForm(data=request.POST,
                                                instance=recipe_comment)
        if recipe_comment_form.is_valid() and recipe_comment.author == request.user:
            recipe_comment = recipe_comment_form.save(commit=False)
            recipe_comment.recipe_post = recipe_post
            recipe_comment.approved = False
            recipe_comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_post_detail', args=[slug]))


def recipe_comment_delete(request, slug, comment_id):
    """
    Delete an individual recipe_comment.

    **Context**

    ``recipe_post``
        An instance of :model:`recipe.RecipePost`.
    ``recipe_comment``
        A single recipe_comment related to the recipe_post.
    """
    recipe_queryset = RecipePost.objects.filter(status=1)
    recipe_post = get_object_or_404(recipe_queryset, slug=slug)
    recipe_comment = get_object_or_404(RecipeComment, pk=comment_id)

    if recipe_comment.author == request.user:
        recipe_comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_post_detail', args=[slug]))


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "recipe/add_recipe.html"
    model = RecipePost
    form_class = RecipePostForm
    success_url = "/recipe/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)
            messages.success(
                self.request,
                "Thanks for submission! It will be published after review.")
            return super(AddRecipe, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a recipe"""
    template_name = 'recipe/edit_recipe.html'
    model = RecipePost
    form_class = RecipePostForm
    success_url = '/recipe/'

    def test_func(self):
        return self.request.user == self.get_object().author


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    template_name = 'recipe/recipe_confirm_delete.html'
    model = RecipePost
    form_class = RecipePostForm
    success_url = '/recipe/'

    def test_func(self):
        return self.request.user == self.get_object().author

    def post(self, request, *args, **kwargs):
        """Handle the post request and delete the recipe."""
        recipe_post = self.get_object()
        recipe_post.delete()
        return redirect('recipe')
