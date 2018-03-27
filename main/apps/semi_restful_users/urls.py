from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.users),
    url(r'^users/new$', views.new_user),
    url(r'^users/(?P<user_id>\d+)$', views.show_user),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit_user),
    url(r'^users/create$', views.create_user),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.delete_user),
    url(r'^users/(?P<user_id>\d+)$', views.update_user),
]
