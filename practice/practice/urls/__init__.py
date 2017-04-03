from django.conf.urls import url, include
from django.contrib import admin
from practice.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^movie$', movie, name="movie"),
    url(r'^about$', about, name="about"),
    url(r'^policy/', include('practice.urls.policy', namespace="policy")),
    url(r'^posts/', include('practice.urls.posts', namespace="posts")),
    url(r'^auth/', include('practice.urls.auth', namespace="auth")),
]
