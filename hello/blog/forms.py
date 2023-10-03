# blog/forms.py

from django import forms
from .models import BlogPost, Comment

# Form for creating or editing a blog post


class BlogPostform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

# Form for adding comments to the blog post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
