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
]
