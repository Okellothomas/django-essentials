from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import BlogPostform, CommentForm

# Create your views here.


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

# View for viewing a single blog post


def view_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view_post', post_id=post_id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/view_post.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# View for creating a new blog post


def create_post(request):
    if request.method == 'POST':
        form = BlogPostform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = BlogPostform()

    return render(render, 'blog/create_post.html', {'form': form})
