from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.index), #open and closed url
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<user_id>\d+)$', views.show), #url parameter the id
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/update$', views.update),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy),
]