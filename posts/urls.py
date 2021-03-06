from django.conf.urls import url
from . import views

app_name ='posts'

urlpatterns = [

    url(r'^create/', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'^author_posts/(?P<fk>[0-9]+)', views.author_posts, name='author_posts'),


]
