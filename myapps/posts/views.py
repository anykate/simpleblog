# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


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


class PostsCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = '__all__'
    pk_url_kwarg = 'post_id'


class PostsUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'body', ]
    pk_url_kwarg = 'post_id'
