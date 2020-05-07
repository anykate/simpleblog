from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category


# Create your views here.
# def index(request):
#     return render(request, 'posts/index.html', {'some_error': 'Error'})


class PostsIndexView(ListView):
    model = Post
    template_name = 'posts/index.html'


class PostsDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/detail.html'


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = '__all__'
    pk_url_kwarg = 'post_id'
    login_url = 'login'


class PostsUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'body', ]
    pk_url_kwarg = 'post_id'
    login_url = 'login'


class PostsDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('posts:index')
    login_url = 'login'


class CategoriesIndexView(ListView):
    model = Category
    template_name = 'posts/categories/index.html'


class CategoriesDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'cat_id'
    template_name = 'posts/categories/detail.html'


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'posts/categories/create.html'
    fields = '__all__'
    login_url = 'login'


class CategoriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'posts/categories/update.html'
    fields = '__all__'
    pk_url_kwarg = 'cat_id'
    login_url = 'login'


class CategoriesDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'posts/categories/delete.html'
    pk_url_kwarg = 'cat_id'
    success_url = reverse_lazy('posts:categories_index')
    login_url = 'login'
