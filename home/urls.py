from django.conf.urls import url
from .views import homepage, contactspage


urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^contacts/$', contactspage, name='contacts'),
]
