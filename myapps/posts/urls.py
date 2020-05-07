from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostsIndexView.as_view(), name='index'),
    path('posts/<int:post_id>/', views.PostsDetailView.as_view(), name='detail'),
]
