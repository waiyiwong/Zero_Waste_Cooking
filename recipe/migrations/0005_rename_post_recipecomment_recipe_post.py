# Generated by Django 4.2.17 on 2025-01-01 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_rename_comment_recipecomment_rename_post_recipepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipecomment',
            old_name='post',
            new_name='recipe_post',
        ),
    ]