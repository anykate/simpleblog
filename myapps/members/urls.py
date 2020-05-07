from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('register/', views.MemberRegisterView.as_view(), name='member_register'),
]
