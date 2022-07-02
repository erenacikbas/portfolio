from django.shortcuts import render
from .models import Post #, BookInstance
from django.views import generic

# Create your views here.
class BlogPostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'blog_post_list' # your own name for the list as a template variable
    template_name = 'blog/index.html' # Specify your own template name/location


class BlogPostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'blog_post' # your own name for the list as a template variable
    template_name = 'blog/single-standard.html'