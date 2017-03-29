from django.conf.urls import url
from practice.views import terms, disclaimer, privacy


urlpatterns = [
    url(r'^terms$', terms, name="terms"),
    url(r'^disclaimer$', disclaimer, name="disclaimer"),
    url(r'^privacy$', privacy, name="privacy"),
        ]
