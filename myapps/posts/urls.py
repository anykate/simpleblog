from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostsIndexView.as_view(), name='index'),
    path('posts/<int:post_id>/', views.PostsDetailView.as_view(), name='detail'),
    path('posts/new/', views.PostsCreateView.as_view(), name='create'),
    path('posts/edit/<int:post_id>/', views.PostsUpdateView.as_view(), name='update'),
    path('posts/delete/<int:post_id>/', views.PostsDeleteView.as_view(), name='delete'),

    path('categories/', views.CategoriesIndexView.as_view(), name='categories_index'),
    path('categories/<int:cat_id>/', views.CategoriesDetailView.as_view(), name='categories_detail'),
    path('categories/<int:cat_id>/posts/', views.CategoriesPostsView.as_view(), name='categories_posts'),
    path('categories/new/', views.CategoriesCreateView.as_view(), name='categories_create'),
    path('categories/edit/<int:cat_id>/', views.CategoriesUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:cat_id>/', views.CategoriesDeleteView.as_view(), name='categories_delete'),
]
