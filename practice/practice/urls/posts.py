from django.conf.urls import url
from practice.views import list, detail, new, create, edit, update, delete, comment_create


urlpatterns = [
    url(r'^list/$', list, name="list"),
    url(r'^(?P<post_id>\d+)/$', detail, name="detail"),
    # CRUD
    url(r'^new/$', new, name="new"),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),

    # Comment
    url(r'^(?P<post_id>\d+)/comment/create$', comment_create, name="comment-create"),
        ]
