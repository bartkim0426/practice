from django.conf.urls import url
from django.contrib import admin
from practice.views import home, room, movie


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^room/(?P<room_id>\d+)$', room),
    url(r'^movie$', movie),
]
