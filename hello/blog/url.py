# blog/urls.py

from django.urls import path
from . import views

# create a list with all the urls

urlpatterns = [
    # URL pattern for te blog homepage
    path('', views.home, name='blog_home'),

    # URL pattern for viewing a single blog post by its ID

    path('post/<int:post_id>/', views.view_post, name='viw_post'),

    # URL pattern for creating a new blog post

    path('creat_post/', views.create_post, name='create_post')
]