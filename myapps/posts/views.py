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
    fields = ['category', 'title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        return super(PostsCreateView, self).form_valid(form)


class PostsUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'body', ]
    pk_url_kwarg = 'post_id'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        this_post = Post.objects.get(id=self.kwargs[self.pk_url_kwarg])
        allowed_to_edit = True if self.request.user.id == this_post.author_id else False
        context = super(PostsUpdateView, self).get_context_data(**kwargs)
        context['allowed_to_edit'] = allowed_to_edit
        return context


class PostsDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('posts:index')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        this_post = Post.objects.get(id=self.kwargs[self.pk_url_kwarg])
        allowed_to_delete = True if self.request.user.id == this_post.author_id else False
        context = super(PostsDeleteView, self).get_context_data(**kwargs)
        context['allowed_to_delete'] = allowed_to_delete
        return context


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


class CategoriesPostsView(DetailView):
    model = Category
    template_name = 'posts/categories/category_posts.html'
    pk_url_kwarg = 'cat_id'
    context_object_name = 'object_list'

    def get_object(self, **kwargs):
        return Post.objects.filter(category_id=self.kwargs[self.pk_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super(CategoriesPostsView, self).get_context_data(**kwargs)
        try:
            context['category'] = Category.objects.get(id=self.kwargs[self.pk_url_kwarg])
        except Category.DoesNotExist:
            context = None
        return context
