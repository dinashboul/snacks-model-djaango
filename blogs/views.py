from django.shortcuts import render
from django.views.generic import  ListView,DetailView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    template_name='blog_list.html'
    model=Post
    context_object_name = 'AllPosts'

class BlogDetailView(DetailView):
    template_name='blogs_detail.html'
    model=Post