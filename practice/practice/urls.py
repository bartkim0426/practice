from django.conf.urls import url, include
from django.contrib import admin
from practice.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^movie$', movie, name="movie"),
    url(r'^about$', about, name="about"),
    url(r'^policy/', include([
        url(r'^terms$', terms, name="terms"),
        url(r'^disclaimer$', disclaimer, name="disclaimer"),
        url(r'^privacy$', privacy, name="privacy"),
             ], namespace="policy"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
