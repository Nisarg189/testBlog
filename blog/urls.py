from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/upvote/$', views.post_upvote, name='post_upvote'),
	url(r'^post/(?P<pk>\d+)/downvote/$', views.post_downvote, name='post_downvote'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
]