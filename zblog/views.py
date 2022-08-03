from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zblog.models import Category, Post
from .forms import PostForm, EditForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-updated_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

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

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '),'category_posts':category_posts, })


def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

