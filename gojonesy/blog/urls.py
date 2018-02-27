from django.conf.urls import include, url
from gojonesy.blog import views

urlpatterns = [
    url(r'^$', views.posts_list, name='blog-index'),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name='blog-detail'),
    url(r'^create/$', views.posts_create, name='blog-create'),
    url(r'^(?P<id>\d+)/edit/$', views.posts_update, name='blog-update'),
    url(r'^(?P<id>\d+)/delete/$', views.posts_delete, name='blog-delete'),

]
