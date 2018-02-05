from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:blogpost_id>/', views.post, name='post')
]