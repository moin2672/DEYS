from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zblog.models import Category, Post
from .forms import PostForm, EditForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-updated_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model=Post
    form_class = PostForm
    template_name ="add_post.html"
    #fields = '__all__'
    # fields = ('title', 'body')

class PostUpdateView(UpdateView):
    model=Post
    form_class = EditForm
    template_name ="update_post.html"
    # fields = ['title', 'title_tag', 'body']


class PostDeleteView(DeleteView):
    model=Post
    template_name ="delete_post.html"
    success_url= reverse_lazy('home')


class CategoryCreateView(CreateView):
    model=Category
    # form_class = PostForm
    template_name ="add_category.html"
    fields = '__all__'
    # fields = ('title', 'body')